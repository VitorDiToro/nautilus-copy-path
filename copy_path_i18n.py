import locale

from gi.repository import GLib

DEFAULT_TRANSLATION = ("Copy Full Path", "Copy Full Paths")

TRANSLATIONS = {
    "en": DEFAULT_TRANSLATION,
    "zh_CN": ("复制完整路径", "复制完整路径"),
    "zh_SG": ("复制完整路径", "复制完整路径"),
    "zh": ("复制完整路径", "复制完整路径"),
    "zh_TW": ("複製完整路徑", "複製完整路徑"),
    "zh_HK": ("複製完整路徑", "複製完整路徑"),
    "zh_MO": ("複製完整路徑", "複製完整路徑"),
    "es_ES": ("Copiar ruta completa", "Copiar rutas completas"),
    "es_MX": ("Copiar ruta completa", "Copiar rutas completas"),
    "es_MS": ("Copiar ruta completa", "Copiar rutas completas"),
    "es_AR": ("Copiar ruta completa", "Copiar rutas completas"),
    "es": ("Copiar ruta completa", "Copiar rutas completas"),
    "pt_BR": ("Copiar caminho completo", "Copiar caminhos completos"),
    "pt_PT": ("Copiar caminho completo", "Copiar caminhos completos"),
    "pt": ("Copiar caminho completo", "Copiar caminhos completos"),
    "ru": ("Копировать полный путь", "Копировать полные пути"),
    "de": ("Vollständigen Pfad kopieren", "Vollständige Pfade kopieren"),
    "fr": ("Copier le chemin complet", "Copier les chemins complets"),
    "ja": ("フルパスをコピー", "フルパスをコピー"),
    "ko": ("전체 경로 복사", "전체 경로 복사"),
    "it": ("Copia percorso completo", "Copia percorsi completi"),
    "pl": ("Kopiuj pełną ścieżkę", "Kopiuj pełne ścieżki"),
    "tr": ("Tam Yolu Kopyala", "Tam Yolları Kopyala"),
    "uk": ("Копіювати повний шлях", "Копіювати повні шляхи"),
}


def get_labels():
    candidates = list(GLib.get_language_names())
    sys_locale = locale.getlocale()[0]
    if sys_locale:
        candidates.append(sys_locale)

    for lang in candidates:
        norm = lang.split(".")[0].split("@")[0].replace("-", "_")
        if norm in TRANSLATIONS:
            return TRANSLATIONS[norm]
        base = norm.split("_")[0]
        if base in TRANSLATIONS:
            return TRANSLATIONS[base]

    return DEFAULT_TRANSLATION
