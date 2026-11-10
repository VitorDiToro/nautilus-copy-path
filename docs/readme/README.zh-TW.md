# Nautilus Copy Full Path

> 為 GNOME Files (Nautilus) 帶來類似 KDE Dolphin 的**複製完整路徑**右鍵選單與 `Ctrl + Alt + C` 快捷鍵。

## 🌐 支援的語言與多語言文件

右鍵選單會自動適配您的系統語言。**點擊下方任意旗幟即可閱讀對應語言的 README 文件：**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## 功能特色

- **右鍵選單：**
  - 選取單一檔案或資料夾：**複製完整路徑**（自動跟隨系統語言）
  - 選取多個項目：**複製完整路徑**（每行一個路徑）
  - 在資料夾空白處右鍵：**複製完整路徑**（複製目前目錄路徑）
- **鍵盤快捷鍵 (`Ctrl + Alt + C`)：**
  - 複製目前選取項目的完整路徑；若未選取任何項目，則複製目前開啟目錄的完整路徑。

## 系統需求

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

## 安裝方式

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

或手動安裝：
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## 參與貢獻

歡迎提交貢獻與翻譯！請參閱 [CONTRIBUTING.md](../../CONTRIBUTING.md) 了解詳情。

## 授權條款

[MIT](../../LICENSE)
