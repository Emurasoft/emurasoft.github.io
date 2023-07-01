# 단어 삭제 명령

### 요약

> 현재 커서의 위치에있는 단어를 삭제합니다.

### 설명

> 두 공백 문자 사이 커서가 위치한 텍스트를 삭제합니다. 이 명령은 커서 위치에 텍스트가 존재 하지 않는 경우 공백을 삭제합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **삭제** \> **단어 삭제**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+DELETE

### 플러그인 명령 ID

- EEID\_DELETE\_WORD (4194)

### 매크로

#### \[JavaScript\]

> document.selection.SelectWord();
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.SelectWord
>
> document.selection.Delete 1
