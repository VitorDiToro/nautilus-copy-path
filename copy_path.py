import shutil

from gi import require_version

require_version("Gdk", "4.0")
require_version("Gtk", "4.0")
require_version("Nautilus", "4.1")

from gi.repository import Gdk, Gio, GLib, GObject, Gtk, Nautilus


class CopyFullPathAction(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        self._selected_paths = []
        self._folder_path = None
        self._shortcut_registered = False
        GLib.idle_add(self._ensure_shortcut)

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

        label = "Copy Full Path" if len(paths) == 1 else "Copy Full Paths"
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

        item = Nautilus.MenuItem(
            name="OmarchyCopyPathNautilus::copy_folder_path",
            label="Copy Full Path",
            icon="edit-copy-symbolic",
        )
        item.connect("activate", self._on_activate, [path])
        return [item]
