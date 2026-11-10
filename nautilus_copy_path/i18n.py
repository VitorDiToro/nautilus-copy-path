from functools import lru_cache
import json
import locale
from pathlib import Path

from gi.repository import GLib

DEFAULT_TRANSLATION = ("Copy Full Path", "Copy Full Paths")
TRANSLATIONS_PATH = Path(__file__).with_name("translations.json")


@lru_cache(maxsize=1)
def load_translations():
    try:
        raw = json.loads(TRANSLATIONS_PATH.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            return {"en": DEFAULT_TRANSLATION}
    except (OSError, ValueError, TypeError):
        return {"en": DEFAULT_TRANSLATION}

    catalog = {}
    for code, entry in raw.items():
        if isinstance(entry, dict):
            one = entry.get("one") or DEFAULT_TRANSLATION[0]
            other = entry.get("other") or DEFAULT_TRANSLATION[1]
            catalog[str(code)] = (str(one), str(other))

    catalog.setdefault("en", DEFAULT_TRANSLATION)
    return catalog


def get_labels(candidates=None):
    translations = load_translations()

    if candidates is None:
        candidates = list(GLib.get_language_names())
        sys_locale = locale.getlocale()[0]
        if sys_locale:
            candidates.append(sys_locale)

    for lang in candidates:
        if not lang:
            continue
        norm = str(lang).split(".")[0].split("@")[0].replace("-", "_")
        if norm in translations:
            return translations[norm]
        base = norm.split("_")[0]
        if base in translations:
            return translations[base]

    return DEFAULT_TRANSLATION
