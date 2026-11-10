# Nautilus Copy Path

> Añade la acción **Copiar ruta** y el atajo `Ctrl + Alt + C` (al estilo de KDE Dolphin) a GNOME Files (Nautilus).

## 🌐 Idiomas Soportados y Documentación

El menú contextual se adapta automáticamente al idioma de tu sistema. **Haz clic en cualquier bandera a continuación para leer este README en ese idioma:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Características

- **Menú contextual (clic derecho):**
  - En un archivo o carpeta: **Copiar ruta** (traducido automáticamente al idioma del sistema)
  - En múltiples elementos seleccionados: **Copiar rutas** (una ruta por línea)
  - En el fondo vacío de una carpeta: **Copiar ruta** (copia la ruta del directorio actual)
- **Atajo de teclado (`Ctrl + Alt + C`):**
  - Copia la ruta completa de los elementos seleccionados o, si no hay nada seleccionado, la ruta del directorio actual.

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

## Instalación

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

O instala manualmente:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp -r copy_path.py nautilus_copy_path ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Contribuir

¡Las contribuciones y traducciones son bienvenidas! Consulta [CONTRIBUTING.md](../../CONTRIBUTING.md) para más detalles.

## Licencia

[MIT](../../LICENSE)
