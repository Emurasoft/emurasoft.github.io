# 왼쪽 문자까지 선택 명령

### 요약

> 왼쪽 문자까지 선택을 확장합니다.

### 설명

> 왼쪽 문자까지 선택을 확장합니다.
> 커서가 줄의 처음에 위치하고 있다면, 이 명령으로 이전 줄의 마지막 점으로 커서를 이동합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **선택 확장** \> **왼쪽 문자까지 선택**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: SHIFT + LEFT ARROW

### 플러그인 명령 ID

- EEID\_SHIFT\_LEFT (4173)

### 매크로

#### \[JavaScript\]

> document.selection.CharLeft(true,1);

#### \[VBScript\]

> document.selection.CharLeft true,1
