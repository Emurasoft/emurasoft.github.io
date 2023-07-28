# 오른쪽 단어 삭제 명령

## 요약

커서의 오른쪽에 있는 단어를 삭제합니다.

## 설명

커서 위치로부터 현재 행의 다음 단어의 첫 문자까지의 텍스트를 삭제합니다. 이 명령은 공백을 삭제합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **삭제** \> **오른쪽 단어 삭제**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+DELETE

## 플러그인 명령 ID

```
EEID_DELETE_RIGHT_WORD (4275)```

## 매크로

### \[JavaScript\]

```
document.selection.WordRight(true,1);
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.WordRight true,1
document.selection.Delete 1
```
