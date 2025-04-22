# 자르기 명령

## 요약

선택 영역이나 현재 줄을 잘라내어 클립보드로 이동합니다.

## 설명

선택 영역이나 현재 줄을 잘라내어 클립보드로 이동합니다.
이 명령 후에 다른 위치로 커서를 움직여 [**붙여넣기** 명령](edit_paste) 을 실행 하여 선택 사항을 붙여 넣을 수 있습니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **자르기**
- [모든 명령](../tools/all_commands): **편집** \> **자르기**
\> **자르기**
- 도구 모음: ![](../../images/cut..png)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+X 또는 SHIFT+DELETE

## 플러그인 명령 ID

```
EEID_EDIT_CUT (4126)
```

## 매크로

### \[JavaScript\]

```
document.selection.cut();
```

### \[VBScript\]

```
document.selection.Cut
```
