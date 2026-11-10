# Nautilus Copy Full Path

> Leve a opção **Copiar caminho completo** e o atalho `Ctrl + Alt + C` (estilo KDE Dolphin) para o GNOME Files (Nautilus).

## 🌐 Idiomas Suportados e Documentação

O menu de contexto se adapta automaticamente ao idioma do seu sistema. **Clique em qualquer bandeira abaixo para ler este README naquele idioma:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Funcionalidades

- **Menu de contexto (botão direito):**
  - Em um arquivo ou pasta: **Copiar caminho completo** (traduzido automaticamente conforme o idioma do sistema)
  - Em múltiplos itens selecionados: **Copiar caminhos completos** (um caminho por linha)
  - No fundo vazio de uma pasta: **Copiar caminho completo** (copia o caminho do diretório atual)
- **Atalho de teclado (`Ctrl + Alt + C`):**
  - Copia o caminho completo dos itens selecionados ou, caso nada esteja selecionado, o caminho do diretório aberto.

## Requisitos

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

## Instalação

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Ou instale manualmente:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Contribuindo

Contribuições e novas traduções são bem-vindas! Veja o arquivo [CONTRIBUTING.md](../../CONTRIBUTING.md) para mais detalhes.

## Licença

[MIT](../../LICENSE)
