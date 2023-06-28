# 오른쪽 단어까지 선택 명령

### 요약

> 오른쪽 단어까지 선택을 확장합니다.

### 설명

> 오른쪽 단어까지 선택을 확장합니다. 이 명령은 단어 뒤에 공백이 있다면, 다음 단어 시작점까지 선택 영역을 확장합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **선택 확장** \> **오른쪽 단어까지 선택**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+RIGHT ARROW

### 플러그인 명령 ID

- EEID\_SHIFT\_RIGHT\_WORD (4174)

### 매크로

#### \[JavaScript\]

> document.selection.WordRight(true,1);

#### \[VBScript\]

> document.selection.WordRight true,1