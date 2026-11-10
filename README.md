# Nautilus Copy Full Path

> Bring KDE Dolphin's **Copy Full Path** action and `Ctrl + Alt + C` shortcut to GNOME Files (Nautilus).

## 🌐 Supported Languages & Documentation

The context menu automatically adapts to your system language. **Click any flag below to read this README in that language:**

[🇺🇸](README.md) [🇬🇧](README.md) [🇧🇷](docs/readme/README.pt-BR.md) [🇵🇹](docs/readme/README.pt-PT.md) [🇪🇸](docs/readme/README.es.md) [🇲🇽](docs/readme/README.es.md) [🇦🇷](docs/readme/README.es.md) [🇨🇳](docs/readme/README.zh-CN.md) [🇹🇼](docs/readme/README.zh-TW.md) [🇭🇰](docs/readme/README.zh-TW.md) [🇷🇺](docs/readme/README.ru.md) [🇩🇪](docs/readme/README.de.md) [🇫🇷](docs/readme/README.fr.md) [🇯🇵](docs/readme/README.ja.md) [🇰🇷](docs/readme/README.ko.md) [🇮🇹](docs/readme/README.it.md) [🇵🇱](docs/readme/README.pl.md) [🇹🇷](docs/readme/README.tr.md) [🇺🇦](docs/readme/README.uk.md)

---

## Features

- **Right-click context menu:**
  - On a single file or folder: **Copy Full Path** (automatically localized to your system language)
  - On multiple selected items: **Copy Full Paths** (one path per line)
  - On the empty background of a folder: **Copy Full Path** (copies the current directory path)
- **Keyboard shortcut (`Ctrl + Alt + C`):**
  - Copies the full path(s) of the currently selected item(s), or the current directory path if nothing is selected.

## Requirements

- `nautilus` (GNOME Files 43+)
- `nautilus-python` (`python3-nautilus` — Debian/Ubuntu, `nautilus-python` — Arch/Fedora)

**Arch Linux / Omarchy:**
```bash
sudo pacman -S --needed nautilus nautilus-python
```

**Ubuntu / Debian:**
```bash
sudo apt install nautilus python3-nautilus
```

**Fedora:**
```bash
sudo dnf install nautilus nautilus-python
```

## Installation

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Or install manually:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp -r copy_path.py nautilus_copy_path ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Contributing

Contributions and translations are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[MIT](LICENSE)
