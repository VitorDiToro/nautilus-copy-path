# Nautilus Copy Path

> Добавляет действие **Копировать путь** и горячую клавишу `Ctrl + Alt + C` (как в KDE Dolphin) в GNOME Files (Nautilus).

## 🌐 Поддерживаемые языки и документация

Контекстное меню автоматически подстраивается под язык вашей системы. **Нажмите на любой флаг ниже, чтобы прочитать этот README на соответствующем языке:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Возможности

- **Контекстное меню (правый клик):**
  - На одном файле или папке: **Копировать путь** (автоматически переводится на язык системы)
  - На нескольких выбранных элементах: **Копировать пути** (по одному пути на строку)
  - На пустом месте в папке: **Копировать путь** (копирует путь текущей папки)
- **Горячая клавиша (`Ctrl + Alt + C`):**
  - Копирует полный путь выбранных элементов или путь текущего каталога, если ничего не выбрано.

## Требования

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

## Установка

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Или установите вручную:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp -r copy_path.py nautilus_copy_path ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Участие в разработке

Мы рады вашим пулреквестам и переводам! Подробности смотрите в [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Лицензия

[MIT](../../LICENSE)
