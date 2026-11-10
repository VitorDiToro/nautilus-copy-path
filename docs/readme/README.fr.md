# Nautilus Copy Full Path

> Ajoute l'action **Copier le chemin complet** et le raccourci `Ctrl + Alt + C` (comme dans KDE Dolphin) à GNOME Files (Nautilus).

## 🌐 Langues prises en charge et documentation

Le menu contextuel s'adapte automatiquement à la langue de votre système. **Cliquez sur un drapeau ci-dessous pour lire ce README dans cette langue :**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Fonctionnalités

- **Menu contextuel (clic droit) :**
  - Sur un fichier ou dossier : **Copier le chemin complet** (traduit automatiquement selon la langue du système)
  - Sur plusieurs éléments sélectionnés : **Copier les chemins complets** (un chemin par ligne)
  - Sur l'arrière-plan vide d'un dossier : **Copier le chemin complet** (copie le chemin du répertoire courant)
- **Raccourci clavier (`Ctrl + Alt + C`) :**
  - Copie le chemin complet des éléments sélectionnés, ou celui du dossier courant si rien n'est sélectionné.

## Prérequis

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

Ou installez manuellement :
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Contribuer

Les contributions et traductions sont les bienvenues ! Consultez [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Licence

[MIT](../../LICENSE)
