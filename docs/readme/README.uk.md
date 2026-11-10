# Nautilus Copy Path

> Додає дію **Копіювати шлях** та комбінацію клавіш `Ctrl + Alt + C` (як у KDE Dolphin) до GNOME Files (Nautilus).

## 🌐 Підтримувані мови та документація

Контекстне меню автоматично адаптується до мови вашої системи. **Натисніть на будь-який прапор нижче, щоб прочитати цей README відповідною мовою:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Можливості

- **Контекстне меню (правий клік):**
  - На одному файлі чи папці: **Копіювати шлях** (автоматично перекладається мовою системи)
  - На кількох вибраних елементах: **Копіювати шляхи** (по одному шляху на рядок)
  - На порожньому місці в папці: **Копіювати шлях** (копіює шлях поточного каталогу)
- **Комбінація клавіш (`Ctrl + Alt + C`):**
  - Копіює повний шлях вибраних елементів або шлях поточного каталогу, якщо нічого не вибрано.

## Вимоги

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

## Встановлення

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Або встановіть вручну:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp -r copy_path.py nautilus_copy_path ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Внесок у проєкт

Будемо раді вашим пулреквестам і перекладам! Детальніше у [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Ліцензія

[MIT](../../LICENSE)
