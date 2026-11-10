# nautilus-copy-path

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

## English

A `nautilus-python` extension (GNOME Files / Nautilus 4.1+ / GTK4) that adds a **Copy Full Path** action (similar to KDE Dolphin), accessible both via the right-click context menu and the `Ctrl + Alt + C` keyboard shortcut.

### Features

- **Right-click context menu:**
  - On a single file or folder: **Copy Full Path** (localized to your system language)
  - On multiple selected items: **Copy Full Paths** (one path per line)
  - On the empty background of a folder: **Copy Full Path** (copies the current directory path)
- **Keyboard shortcut (`Ctrl + Alt + C`):**
  - Copies the full path(s) of the currently selected item(s), or the current directory path if nothing is selected.
- **Supported languages (automatic system locale detection):**
  - English (`en`), Português (`pt_BR`, `pt_PT`), Español (`es_ES`, `es_MX`, `es_MS`, `es_AR`), 简体中文 (`zh_CN`), 繁體中文 (`zh_TW`, `zh_HK`), Русский (`ru`), Deutsch (`de`), Français (`fr`), 日本語 (`ja`), 한국어 (`ko`), Italiano (`it`), Polski (`pl`), Türkçe (`tr`), Українська (`uk`).

### Requirements

- `nautilus` (GNOME Files 43+)
- `nautilus-python` (`python3-nautilus` on Debian/Ubuntu, `nautilus-python` on Arch/Fedora)

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

### Installation

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Or manually:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

### License

[MIT](LICENSE)

---

## Português

Extensão `nautilus-python` (GNOME Files / Nautilus 4.1+ / GTK4) que adiciona a função **Copiar caminho completo** / **Copy Full Path** (como no KDE Dolphin), acessível tanto pelo menu de contexto (botão direito) quanto pelo atalho de teclado `Ctrl + Alt + C`.

### Funcionalidades

- **Menu de contexto (botão direito):**
  - Em um arquivo ou pasta: **Copiar caminho completo** (segue automaticamente o idioma do sistema)
  - Em múltiplos itens selecionados: **Copiar caminhos completos** (um caminho por linha)
  - No fundo vazio de uma pasta: **Copiar caminho completo** (copia o caminho do diretório atual)
- **Atalho de teclado (`Ctrl + Alt + C`):**
  - Copia o caminho completo dos itens selecionados ou, caso nada esteja selecionado, o caminho do diretório aberto.
- **Idiomas suportados (detecção automática do idioma do sistema):**
  - Português (`pt_BR`, `pt_PT`), Inglês (`en`), Espanhol (`es_ES`, `es_MX`, `es_MS`, `es_AR`), Chinês Simplificado (`zh_CN`), Chinês Tradicional (`zh_TW`, `zh_HK`), Russo (`ru`), Alemão (`de`), Francês (`fr`), Japonês (`ja`), Coreano (`ko`), Italiano (`it`), Polonês (`pl`), Turco (`tr`), Ucraniano (`uk`).

### Requisitos

- `nautilus` (GNOME Files 43+)
- `nautilus-python` (`python3-nautilus` no Debian/Ubuntu, `nautilus-python` no Arch/Fedora)

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

### Instalação

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Ou manualmente:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

### Licença

[MIT](LICENSE)
