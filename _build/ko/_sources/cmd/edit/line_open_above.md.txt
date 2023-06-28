# 위쪽에 줄 열기 명령

### 요약

> 현재 커서 위치 위쪽에 새로운 줄을 삽입합니다.

### 설명

> 현재 커서가 위치해 있는 위쪽 행에 새로운 줄을 삽입합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **삽입**
\> **위쪽에 줄 열기**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: SHIFT+ENTER

### 플러그인 명령 ID

- EEID\_LINE\_OPEN\_ABOVE (4195)

### 매크로

#### \[JavaScript\]

> document.selection.LineOpen(true);

#### \[VBScript\]

> document.selection.LineOpen true