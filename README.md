# nautilus-copy-path

Extensão `nautilus-python` (GNOME Files / Nautilus 4.1+ / GTK4) que adiciona a função **Copy Full Path** (como no Dolphin), acessível tanto pelo menu de contexto (botão direito) quanto pelo atalho de teclado `Ctrl + Alt + C`.

## Funcionalidades

- **Menu de contexto (botão direito):**
  - Em um arquivo ou pasta: **Copy Full Path**
  - Em múltiplos itens selecionados: **Copy Full Paths** (um caminho por linha)
  - No fundo vazio de uma pasta: **Copy Full Path** (copia o caminho do diretório atual)
- **Atalho `Ctrl + Alt + C`:**
  - Copia o caminho completo dos itens selecionados ou, caso nada esteja selecionado, o caminho do diretório aberto.

## Requisitos

- `nautilus` (GNOME Files 43+)
- `nautilus-python` (`python-nautilus` em distros baseadas em Debian/Ubuntu)

No Arch Linux / Omarchy:
```bash
sudo pacman -S --needed nautilus nautilus-python
```

## Instalação

```bash
./install.sh
```

Ou manualmente:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```
