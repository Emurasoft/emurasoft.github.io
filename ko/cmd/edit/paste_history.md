# 클립보드 링 순환 명령

## 요약

커서 위치에 클립보드 사용 기록중 하나의 내용을 순환하여 붙여 넣습니다.

## 설명

커서 위치에 클립보드 사용 기록중 (최근에 복사된 항목) 하나의 내용을 순환하여 붙여 넣습니다.
이 명령을 반복적으로 선택하면 클립보드 사용 기록에 있는 항목들을 순환할 것입니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **클립보드 링 순환**
- [모든 명령](../tools/all_commands): **편집** \> **붙여넣기**
\> **클립보드 링 순환**
- 도구 모음: ![](../../images/cycle_clipboard_ring..png)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+V, CTRL+SHIFT+INSERT

## 플러그인 명령 ID

```
EEID_PASTE_HISTORY (4454)
```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID (4454);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4454
```
