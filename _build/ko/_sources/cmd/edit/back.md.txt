# 왼쪽 문자 삭제 명령

### 요약

> 선택 범위를 삭제하거나 또는 커서의 왼쪽 문자를 삭제합니다.

### 설명

> (만약 존재한다면) 선택된 텍스트를 삭제하거나, 또는 선택된 텍스트가 없다면 커서의 왼쪽 문자를 삭제합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **삭제** \> **왼쪽 문자 삭제**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: Backspace

### 플러그인 명령 ID

- EEID\_BACK (4186)

### 매크로

#### \[JavaScript\]

> document.selection.DeleteLeft(1);

#### \[VBScript\]

> document.selection.DeleteLeft 1