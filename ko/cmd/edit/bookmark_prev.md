# 이 그룹의 이전 책갈피 명령

## 요약

이 그룹의 이전 책갈피로 이동합니다.

## 설명

커서를 이 그룹의 이전 책갈피로 이동합니다.
현재 문서에 책갈피가 존재하지 않는 경우, 이 명령은 다음 문서의 마지막 책갈피로 이동합니다.
오직 하나의 문서만 책갈피를 포함하고 있는 경우, 즉시 그 문서의 마지막 책갈피로 이동합니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **책갈피** \> **이 그룹** \> **이전 책갈피**
- [모든 명령](../tools/all_commands): **편집** \> **책갈피** \> **이 그룹** \> **이전 책갈피**
- 도구 모음: ![](../../images/bookmarkprev.png)
- 상태 표시줄: 없음
- 기본 바로 가기 키: SHIFT+F2

## 플러그인 명령 ID

```
EEID_BOOKMARK_PREV (4322)
```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4322);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4322
```
