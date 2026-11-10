import locale
import shutil

from gi import require_version

require_version("Gdk", "4.0")
require_version("Gtk", "4.0")
require_version("Nautilus", "4.1")

from gi.repository import Gdk, Gio, GLib, GObject, Gtk, Nautilus

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


class CopyFullPathAction(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        self._selected_paths = []
        self._folder_path = None
        self._shortcut_registered = False
        GLib.idle_add(self._ensure_shortcut)

    def _get_labels(self):
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

    def _ensure_shortcut(self):
        if self._shortcut_registered:
            return False

        app = Gio.Application.get_default()
        if not isinstance(app, Gtk.Application):
            return False

        action = Gio.SimpleAction.new("copy-full-path", None)
        action.connect("activate", self._on_shortcut_activate)
        app.add_action(action)
        app.set_accels_for_action("app.copy-full-path", ["<Control><Alt>c"])
        self._shortcut_registered = True
        return False

    def _copy_paths(self, paths):
        if not paths:
            return

        text = "\n".join(paths)
        display = Gdk.Display.get_default()
        if display:
            clipboard = display.get_clipboard()
            if clipboard:
                clipboard.set(text)
                return

        wl_copy = shutil.which("wl-copy")
        if wl_copy:
            Gio.Subprocess.new([wl_copy, "--", text], Gio.SubprocessFlags.NONE)

    def _extract_path(self, file_info):
        if not file_info:
            return None
        location = file_info.get_location()
        if not location:
            return None
        return location.get_path() or location.get_uri()

    def _selected_file_paths(self, files):
        paths = []
        seen = set()

        for file_info in files or []:
            path = self._extract_path(file_info)
            if path and path not in seen:
                seen.add(path)
                paths.append(path)

        return paths

    def _on_activate(self, _menu, paths):
        self._copy_paths(paths)

    def _on_shortcut_activate(self, _action, _param):
        if self._selected_paths:
            self._copy_paths(self._selected_paths)
        elif self._folder_path:
            self._copy_paths([self._folder_path])

    def get_file_items(self, *args):
        self._ensure_shortcut()
        files = args[0] if len(args) == 1 else args[1]
        paths = self._selected_file_paths(files)
        self._selected_paths = paths

        if not paths:
            return []

        single_label, plural_label = self._get_labels()
        label = single_label if len(paths) == 1 else plural_label
        item = Nautilus.MenuItem(
            name="OmarchyCopyPathNautilus::copy_full_path",
            label=label,
            icon="edit-copy-symbolic",
        )
        item.connect("activate", self._on_activate, paths)
        return [item]

    def get_background_items(self, *args):
        self._ensure_shortcut()
        folder = args[0] if len(args) == 1 else args[1]
        path = self._extract_path(folder)
        self._folder_path = path

        if not path:
            return []

        single_label, _ = self._get_labels()
        item = Nautilus.MenuItem(
            name="OmarchyCopyPathNautilus::copy_folder_path",
            label=single_label,
            icon="edit-copy-symbolic",
        )
        item.connect("activate", self._on_activate, [path])
        return [item]
