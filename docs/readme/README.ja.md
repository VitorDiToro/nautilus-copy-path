# Nautilus Copy Full Path

> KDE Dolphin のような **フルパスをコピー** 右クリックメニューと `Ctrl + Alt + C` ショートカットを GNOME Files (Nautilus) に追加します。

## 🌐 対応言語とドキュメント

コンテキストメニューはシステム言語に自動的に適応します。**以下の国旗をクリックすると、その言語で README を読むことができます：**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## 機能

- **右クリックコンテキストメニュー：**
  - 単一のファイルまたはフォルダ：**フルパスをコピー**（システム言語に自動対応）
  - 複数のアイテムを選択時：**フルパスをコピー**（1行に1パス）
  - フォルダの空白部分：**フルパスをコピー**（現在のディレクトリパスをコピー）
- **キーボードショートカット (`Ctrl + Alt + C`)：**
  - 選択中のアイテムのフルパスをコピーします。何も選択されていない場合は現在のフォルダのパスをコピーします。

## 必要要件

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

## インストール

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

または手動でインストール：
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## コントリビューション

コントリビューションや翻訳の追加を歓迎します！詳細は [CONTRIBUTING.md](../../CONTRIBUTING.md) をご覧ください。

## ライセンス

[MIT](../../LICENSE)
