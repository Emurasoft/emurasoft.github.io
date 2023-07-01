# 오른쪽 문자로 명령

### 요약

> 커서를 한 문자 오른쪽으로 이동합니다.

### 설명

> 커서를 한 문자 오른쪽으로 이동합니다.
> 커서가 줄의 마지막에 위치하고 있다면, 이 명령으로 다음 줄의 시작점으로 커서를 이동합니다.
> 오른쪽 화살표키를 한번 누르는 것과 동일시 작용됩니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **가로로 커서 이동** \> **오른쪽 문자로**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: RIGHT ARROW

### 플러그인 명령 ID

- EEID\_RIGHT (4156)

### 매크로

#### \[JavaScript\]

> document.selection.CharRight(false,1);

#### \[VBScript\]

> document.selection.CharRight false,1
