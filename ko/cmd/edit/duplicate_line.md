# 줄 복제 명령

## 요약

현재 로직 줄을 복제합니다.

## 설명

현재 커서의 위치 아래에 현재 로직 줄의 복사본을 삽입합니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **고급**
\> **줄 복제**
- [모든 명령](../tools/all_commands): **편집** \> **삽입**
\> **줄 복제**
- 도구 모음: ![](../../images/duplicateline.png)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+Y

## 플러그인 명령 ID

```
EEID_DUPLICATE_LINE (4328)
```

## 매크로

### \[JavaScript\]

```
document.selection.DuplicateLine();
```

### \[VBScript\]

```
document.selection.DuplicateLine
```
