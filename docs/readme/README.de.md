# Nautilus Copy Full Path

> Bringt die Aktion **Vollständigen Pfad kopieren** und das Tastenkürzel `Ctrl + Alt + C` (wie in KDE Dolphin) in GNOME Files (Nautilus).

## 🌐 Unterstützte Sprachen & Dokumentation

Das Kontextmenü passt sich automatisch Ihrer Systemsprache an. **Klicken Sie unten auf eine Flagge, um dieses README in der jeweiligen Sprache zu lesen:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Funktionen

- **Rechtsklick-Kontextmenü:**
  - Bei einer einzelnen Datei oder einem Ordner: **Vollständigen Pfad kopieren** (automatisch in Ihrer Systemsprache)
  - Bei mehreren ausgewählten Elementen: **Vollständige Pfade kopieren** (ein Pfad pro Zeile)
  - Auf dem leeren Hintergrund eines Ordners: **Vollständigen Pfad kopieren** (kopiert den Pfad des aktuellen Ordners)
- **Tastenkürzel (`Ctrl + Alt + C`):**
  - Kopiert den vollständigen Pfad der ausgewählten Elemente oder den aktuellen Ordnerpfad, wenn nichts ausgewählt ist.

## Voraussetzungen

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

Oder manuell installieren:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Mitwirken

Beiträge und Übersetzungen sind willkommen! Siehe [CONTRIBUTING.md](../../CONTRIBUTING.md) für Richtlinien.

## Lizenz

[MIT](../../LICENSE)
