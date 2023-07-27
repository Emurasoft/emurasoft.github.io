# 삽입/덮어쓰기를 설정/해제하기 명령

## 요약

삽입/덮어쓰기를 설정/해제합니다.

## 설명

삽입/덮어쓰기를 설정/해제합니다. 엠에디터는 일반적으로 삽입 모드로 시작합니다.
엠에디터가 삽입 모드인 경우, 커서는 "I" 모양을 하고 문자를 삽입하며 기존 문자를 삭제하지 않습니다.
엠에디터가 덮어쓰기 모드인 경우, 커서는 사각형 모양이 되며 문자를 삽입할 때 기존의 문자를 삭제하며 새로운 문자로 덮어씁니다.
이 명령은 삽입/덮어쓰기를 설정/해제합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>삽입
\>삽입/덮어쓰기를 설정/해제하기
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: Insert

## 플러그인 명령 ID

```
EEID_INSERT (4142)```

## 매크로

### \[JavaScript\]

```
document.selection.OverwriteMode = !document.selection.OverwriteMode;
```

### \[VBScript\]

```
document.selection.OverwriteMode = NOT document.selection.OverwriteMode
```
