# Nautilus Copy Full Path

> 为 GNOME Files (Nautilus) 带来类似 KDE Dolphin 的**复制完整路径**右键菜单与 `Ctrl + Alt + C` 快捷键。

## 🌐 支持的语言与多语言文档

右键菜单会自动适配您的系统语言。**点击下方任意国旗/地区旗帜即可阅读对应语言的 README 文档：**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## 功能特性

- **右键上下文菜单：**
  - 选中单个文件或文件夹：**复制完整路径**（自动跟随系统语言）
  - 选中多个项目：**复制完整路径**（每行一个路径）
  - 在文件夹空白处右键：**复制完整路径**（复制当前目录路径）
- **键盘快捷键 (`Ctrl + Alt + C`)：**
  - 复制当前选中项目的完整路径；如果未选中任何内容，则复制当前打开目录的完整路径。

## 环境要求

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

## 安装方法

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

或手动安装：
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp copy_path.py copy_path_i18n.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## 参与贡献

欢迎提交代码与翻译！请参阅 [CONTRIBUTING.md](../../CONTRIBUTING.md) 了解详情。

## 开源协议

[MIT](../../LICENSE)
