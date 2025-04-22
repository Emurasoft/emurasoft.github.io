# 책갈피 설정/해제 명령

## 요약

현재 줄에 책갈피를 설정/해제 합니다.

## 설명

책갈피가 설정되어 있지 않다면 현재 줄에 책갈피를 설정 하고, 설정되어 있다면 초기화 합니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **책갈피** \> **책갈피 설정/해제**
- [모든 명령](../tools/all_commands): **편집** \> **책갈피** \> **책갈피 설정/해제**
- 도구 모음: ![](../../images/bookmarktoggle.png)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+F2

## 플러그인 명령 ID

```
EEID_BOOKMARK_TOGGLE (4320)
```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4320);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4320
```
