# 오른쪽 단어 명령

### 요약

> 커서를 한 단어 오른쪽으로 이동합니다.

### 설명

> 커서를 한 단어 오른쪽으로 이동합니다.
> 이 명령은 공백을 무시하고 커서를 현재 행의 다음 단어의 시작점으로 이동합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **가로로 커서 이동** \> **오른쪽 단어**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+RIGHT ARROW

### 플러그인 명령 ID

- EEID\_RIGHT\_WORD (4158)

### 매크로

#### \[JavaScript\]

> document.selection.WordRight(false,1);

#### \[VBScript\]

> document.selection.WordRight false,1