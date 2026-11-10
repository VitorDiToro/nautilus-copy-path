# Nautilus Copy Full Path

> Dodaje akcję **Kopiuj pełną ścieżkę** oraz skrót `Ctrl + Alt + C` (znane z KDE Dolphin) do GNOME Files (Nautilus).

## 🌐 Obsługiwane Języki i Dokumentacja

Menu kontekstowe automatycznie dostosowuje się do języka systemu. **Kliknij dowolną flagę poniżej, aby przeczytać ten plik README w wybranym języku:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Funkcje

- **Menu kontekstowe (prawy przycisk myszy):**
  - Na pojedynczym pliku lub katalogu: **Kopiuj pełną ścieżkę** (automatycznie w języku systemu)
  - Na wielu zaznaczonych elementach: **Kopiuj pełne ścieżki** (jedna ścieżka w każdym wierszu)
  - Na pustym tle katalogu: **Kopiuj pełną ścieżkę** (kopiuje ścieżkę bieżącego katalogu)
- **Skrót klawiszowy (`Ctrl + Alt + C`):**
  - Kopiuje pełną ścieżkę zaznaczonych elementów lub ścieżkę bieżącego katalogu, jeśli nic nie zaznaczono.

## Wymagania

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

## Instalacja

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Lub zainstaluj ręcznie:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py copy_path_i18n.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Współtworzenie

Zgłoszenia i tłumaczenia są mile widziane! Zobacz [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Licencja

[MIT](../../LICENSE)
