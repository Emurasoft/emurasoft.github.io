# 논리 홈 명령

### 요약

> 현재 논리 줄의 처음으로 커서를 이동합니다.

### 설명

> 현재 논리 줄의 처음으로 커서를 이동합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **가로로 커서 이동** \> **논리 홈**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: ALT+HOME

### 플러그인 명령 ID

- EEID\_LOGICAL\_HOME (4165)

### 매크로

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineLogical);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineLogical
