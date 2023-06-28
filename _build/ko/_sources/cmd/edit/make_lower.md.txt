# 소문자로 명령

### 요약

> 선택 영역을 모두 소문자로 변환합니다.

### 설명

> 선택 영역을 모두 소문자로 변환합니다. 예를 들어, A는 a가 되며 Ä는 ä로, Λ는 λ가 됩니다.

### 실행하는 방법

- 기본 메뉴: **편집** \> **선택 변환** \> **소문자로**
- [모든 명령](../tools/all_commands): **편집** > **선택 변환** \> **소문자로**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+U

### 플러그인 명령 ID

- EEID\_MAKE\_LOWER (4150)

### 매크로

#### \[JavaScript\]

> document.selection.ChangeCase(eeCaseLowerCase);

#### \[VBScript\]

> document.selection.ChangeCase eeCaseLowerCase