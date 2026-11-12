import shutil
import weakref

from gi import require_version

require_version("Gdk", "4.0")
require_version("Gtk", "4.0")
require_version("Nautilus", "4.1")

from gi.repository import Gdk, Gio, GLib, GObject, Gtk, Nautilus

try:
    from nautilus_copy_path.i18n import get_labels
except ImportError:
    def get_labels():
        return ("Copy Path", "Copy Paths")

SHORTCUT_ACCEL = "<Control><Alt>c"
MENU_ACTION_SUFFIXES = (
    "OmarchyCopyPathNautilus%3A%3Acopy_full_path",
    "OmarchyCopyPathNautilus%3A%3Acopy_folder_path",
)
MENU_ACTION_NAMES = tuple(
    f"view.extension_extensions_{idx}_{suffix}"
    for idx in range(16)
    for suffix in MENU_ACTION_SUFFIXES
)


class CopyFullPathAction(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        self._selected_paths = []
        self._folder_path = None
        self._shortcut_registered = False
        self._action = None
        self._action_handler_id = 0
        self._window_added_handler_id = 0
        self._shutdown_handler_id = 0
        self._configured_windows = weakref.WeakSet()
        self._idle_id = GLib.idle_add(self._on_idle_ensure_shortcut)

    def _on_idle_ensure_shortcut(self):
        self._idle_id = 0
        self._ensure_shortcut()
        return False

    def _attach_menu_accels(self, window):
        if not isinstance(window, Gtk.Widget) or window in self._configured_windows:
            return

        controller = Gtk.ShortcutController()
        controller.set_scope(Gtk.ShortcutScope.MANAGED)
        controller.set_propagation_phase(Gtk.PropagationPhase.NONE)

        for action_name in MENU_ACTION_NAMES:
            trigger = Gtk.ShortcutTrigger.parse_string(SHORTCUT_ACCEL)
            action = Gtk.NamedAction.new(action_name)
            controller.add_shortcut(Gtk.Shortcut.new(trigger, action))

        window.add_controller(controller)
        self._configured_windows.add(window)

    def _on_window_added(self, _app, window):
        self._attach_menu_accels(window)

    def _on_app_shutdown(self, app):
        if self._idle_id:
            GLib.source_remove(self._idle_id)
            self._idle_id = 0

        if self._action is not None:
            if self._action_handler_id:
                self._action.disconnect(self._action_handler_id)
                self._action_handler_id = 0
            self._action = None

        if isinstance(app, Gtk.Application):
            app.set_accels_for_action("app.copy-full-path", [])

        if isinstance(app, Gio.ActionMap):
            app.remove_action("copy-full-path")

        if self._window_added_handler_id:
            app.disconnect(self._window_added_handler_id)
            self._window_added_handler_id = 0

        if self._shutdown_handler_id:
            app.disconnect(self._shutdown_handler_id)
            self._shutdown_handler_id = 0

        self._configured_windows.clear()
        self._shortcut_registered = False

    def _ensure_shortcut(self):
        if self._idle_id:
            GLib.source_remove(self._idle_id)
            self._idle_id = 0

        app = Gio.Application.get_default()
        if not isinstance(app, Gtk.Application):
            return False

        if not self._shortcut_registered:
            action = Gio.SimpleAction.new("copy-full-path", None)
            self._action_handler_id = action.connect(
                "activate", self._on_shortcut_activate
            )
            app.add_action(action)
            app.set_accels_for_action("app.copy-full-path", [SHORTCUT_ACCEL])
            self._window_added_handler_id = app.connect(
                "window-added", self._on_window_added
            )
            self._shutdown_handler_id = app.connect(
                "shutdown", self._on_app_shutdown
            )
            self._action = action
            self._shortcut_registered = True

        for window in app.get_windows():
            self._attach_menu_accels(window)

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

        single_label, plural_label = get_labels()
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

        single_label, _ = get_labels()
        item = Nautilus.MenuItem(
            name="OmarchyCopyPathNautilus::copy_folder_path",
            label=single_label,
            icon="edit-copy-symbolic",
        )
        item.connect("activate", self._on_activate, [path])
        return [item]
