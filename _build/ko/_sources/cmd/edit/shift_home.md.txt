# 홈 선택 명령

### 요약

> 현재 줄의 시작부분으로 선택을 확장합니다.

### 설명

> 현재 줄의 시작부분으로 선택을 확장합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **선택 확장** \> **홈 선택**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_SHIFT\_HOME (4180)

### 매크로

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineView);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineView