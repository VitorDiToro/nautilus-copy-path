# Nautilus Copy Path

> KDE Dolphin 스타일의 **경로 복사** 우클릭 메뉴와 `Ctrl + Alt + C` 단축키를 GNOME Files (Nautilus)에 추가합니다.

## 🌐 지원 언어 및 문서

우클릭 컨텍스트 메뉴는 시스템 언어에 맞춰 자동으로 표시됩니다. **아래 국기를 클릭하면 해당 언어로 작성된 README를 읽을 수 있습니다:**

[🇺🇸](../../README.md) [🇬🇧](../../README.md) [🇧🇷](README.pt-BR.md) [🇵🇹](README.pt-PT.md) [🇪🇸](README.es.md) [🇲🇽](README.es.md) [🇦🇷](README.es.md) [🇨🇳](README.zh-CN.md) [🇹🇼](README.zh-TW.md) [🇭🇰](README.zh-TW.md) [🇷🇺](README.ru.md) [🇩🇪](README.de.md) [🇫🇷](README.fr.md) [🇯🇵](README.ja.md) [🇰🇷](README.ko.md) [🇮🇹](README.it.md) [🇵🇱](README.pl.md) [🇹🇷](README.tr.md) [🇺🇦](README.uk.md)

---

## 주요 기능

- **우클릭 컨텍스트 메뉴:**
  - 단일 파일 또는 폴더: **경로 복사** (시스템 언어 자동 감지)
  - 여러 항목 선택 시: **경로 복사** (줄바꿈으로 구분)
  - 폴더의 빈 공간 우클릭: **경로 복사** (현재 디렉터리 경로 복사)
- **키보드 단축키 (`Ctrl + Alt + C`):**
  - 선택된 항목의 전체 경로를 복사하며, 선택된 항목이 없으면 현재 폴더의 경로를 복사합니다.

## 필수 조건

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

## 설치 방법

```bash
git clone https://github.com/VitorDiToro/nautilus-copy-path.git
cd nautilus-copy-path
./install.sh
```

또는 수동 설치:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp -r copy_path.py nautilus_copy_path ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## 기여하기

기여와 번역 참여를 환영합니다! 자세한 내용은 [CONTRIBUTING.md](../../CONTRIBUTING.md)를 참고하세요.

## 라이선스

[MIT](../../LICENSE)
