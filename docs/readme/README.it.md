# Nautilus Copy Path

> Porta l'azione **Copia percorso** e la scorciatoia `Ctrl + Alt + C` (in stile KDE Dolphin) su GNOME Files (Nautilus).

## 🌐 Lingue Supportate e Documentazione

Il menu contestuale si adatta automaticamente alla lingua di sistema. **Clicca su una bandiera qui sotto per leggere questo README nella tua lingua:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Funzionalità

- **Menu contestuale (clic destro):**
  - Su un singolo file o cartella: **Copia percorso** (localizzato automaticamente nella lingua di sistema)
  - Su più elementi selezionati: **Copia percorsi** (un percorso per riga)
  - Sullo sfondo vuoto di una cartella: **Copia percorso** (copia il percorso della cartella corrente)
- **Scorciatoia da tastiera (`Ctrl + Alt + C`):**
  - Copia il percorso completo degli elementi selezionati o, se non è selezionato nulla, il percorso della cartella corrente.

## Requisiti

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

## Installazione

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Oppure installa manualmente:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp -r copy_path.py nautilus_copy_path ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Contribuire

Contributi e traduzioni sono benvenuti! Consulta [CONTRIBUTING.md](../../CONTRIBUTING.md) per le linee guida.

## Licenza

[MIT](../../LICENSE)
