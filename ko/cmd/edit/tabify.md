# 탭 지정 명령

### 요약

> 해당하는 공백을 탭으로 변환합니다.

### 설명

> 각 행의 시작 부분에 선택된 공백을 탭으로 변환합니다.
> 변환되는 공백의 수는 [**탭/들여쓰기** 대화 상자](../../dlg/properties/general/indent/index) 에서 설정할 수 있는 탭 설정 공간의 수와 일치해야 합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **선택 변환** \> **탭 지정**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_TABIFY (4356)

### 매크로

#### \[JavaScript\]

> document.selection.Tabify();

#### \[VBScript\]

> document.selection.Tabify