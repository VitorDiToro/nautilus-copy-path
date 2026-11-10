# Nautilus Copy Full Path

> KDE Dolphin'deki **Tam Yolu Kopyala** seçeneğini ve `Ctrl + Alt + C` kısayolunu GNOME Files (Nautilus) uygulamasına kazandırır.

## 🌐 Desteklenen Diller ve Dokümantasyon

Sağ tık menüsü sistem dilinize otomatik olarak uyum sağlar. **Bu README dosyasını ilgili dilde okumak için aşağıdaki bayraklardan birine tıklayın:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## Özellikler

- **Sağ tık bağlam menüsü:**
  - Tek bir dosya veya klasörde: **Tam Yolu Kopyala** (sistem dilinize göre otomatik çevrilir)
  - Birden fazla seçili öğede: **Tam Yolları Kopyala** (her satırda bir yol)
  - Klasörün boş alanında: **Tam Yolu Kopyala** (mevcut dizin yolunu kopyalar)
- **Klavye kısayolu (`Ctrl + Alt + C`):**
  - Seçili öğelerin tam yolunu, hiçbir şey seçili değilse mevcut klasörün tam yolunu kopyalar.

## Gereksinimler

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

## Kurulum

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

Veya manuel olarak kurun:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py copy_path_i18n.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Katkıda Bulunma

Katkılarınız ve çevirileriniz memnuniyetle karşılanır! Yönergeler için [CONTRIBUTING.md](../../CONTRIBUTING.md) dosyasına bakın.

## Lisans

[MIT](../../LICENSE)
