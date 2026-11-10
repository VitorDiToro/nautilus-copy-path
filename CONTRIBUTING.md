# Contributing to nautilus-copy-path

## Dev setup

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

`nautilus` (GNOME Files 43+, GTK4) and `nautilus-python` (`python3-nautilus` on Debian/Ubuntu) are required. The extension has no external Python package dependencies beyond standard library modules and the system PyGObject bindings (`Gdk 4.0`, `Gtk 4.0`, `Nautilus 4.1`) loaded by Nautilus itself.

## Commit attribution

GitHub associates commits with accounts through the author email stored in each commit. Before pushing a branch, inspect every commit that the pull request will add:

```bash
git log --format='%h %an <%ae>' "$(git merge-base HEAD origin/main)"..HEAD
```

Use an email verified by your GitHub account, or its GitHub-provided `noreply` address. Set it for this checkout when your global Git identity belongs to a different project or employer:

```bash
git config --local user.name "Your Name"
git config --local user.email "your-verified-address@example.com"
```

Correct attribution mistakes on the pull-request branch before it is merged. The project does not rewrite shared `main` history solely to change attribution.

## Required checks before push/merge

Run these checks locally before opening a pull request:

```bash
python3 -m py_compile copy_path.py
bash -n install.sh
git diff --check
./install.sh
```

To verify that Nautilus loads the extension cleanly without Python tracebacks or warnings, stop any running background instance and run Nautilus in the foreground:

```bash
nautilus -q
nautilus --new-window
```

## Workflow rules

1. **Keep changes small and scoped to the task.** Avoid unrelated refactors or bundling multiple independent changes in a single pull request.
2. **Single-file extension architecture.** Keep the extension self-contained in `copy_path.py` so users can install it by copying a single file into `~/.local/share/nautilus-python/extensions/`.
3. **Zero external dependencies.** Rely only on Python's standard library and the GI bindings already loaded by Nautilus (`Gdk`, `Gio`, `GLib`, `GObject`, `Gtk`, `Nautilus`).
4. **No dead code or speculative abstractions.** Write comments only to explain *why* something non-obvious is done, never *what* the line already says.
5. **Test before claiming done.** Verify single-item selection, multi-item selection, empty folder background click, and the `Ctrl + Alt + C` shortcut.

## Technical invariants

- **Never block the Nautilus main loop.** Nautilus invokes `get_file_items` and `get_background_items` on the GTK main thread whenever the selection or active directory changes. Never perform synchronous I/O, network requests, or blocking `subprocess.run()` calls inside those methods.
- **Safe clipboard and subprocess handling.** Always prefer the native in-process GTK4 clipboard (`Gdk.Display.get_default().get_clipboard().set(text)`). When falling back to `wl-copy`, spawn it asynchronously via `Gio.Subprocess.new([wl_copy, "--", text], Gio.SubprocessFlags.NONE)`—never pass file paths through a shell (`shell=True`).
- ** Dual-signature compatibility for `MenuProvider`.** Keep `*args` handling (`args[0] if len(args) == 1 else args[1]`) in `get_file_items` and `get_background_items` so the extension works across Nautilus 4.0 and 4.1+ callback signatures.

## Translations

Context menu labels are stored in the `TRANSLATIONS` dictionary in `copy_path.py` as `(singular, plural)` tuples and resolved at runtime via `GLib.get_language_names()` and `locale.getlocale()`.

When adding or updating a translation:

1. Add the locale entry (`lang_REGION` and/or base `lang` code) to `TRANSLATIONS` in `copy_path.py` with both singular and plural forms:
   ```python
   "pt_BR": ("Copiar caminho completo", "Copiar caminhos completos"),
   ```
   For languages that do not distinguish singular and plural in menu labels (e.g., `zh_CN`, `zh_TW`, `ja`, `ko`), provide the same string for both elements of the tuple.
2. Verify language resolution from the command line:
   ```bash
   LANGUAGE=pt_BR python3 -c 'import copy_path; print(copy_path.CopyFullPathAction()._get_labels())'
   ```
3. Add the corresponding flag to the `Supported languages / Idiomas suportados` section in `README.md`.
