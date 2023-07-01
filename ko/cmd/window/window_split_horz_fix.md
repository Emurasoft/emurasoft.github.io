# 가로 분할 후 위치 고정 명령

### 요약

> S현재 창을 수평으로 분할한 후 분할된 위치를 고정합니다.

### 설명

> 이 명령은 현재 창을 두 개의 수평한 창으로 분할하고, 즉시 창의 중앙에 분할 위치를 고정합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **창** \> **분할** \> **가로 분할 후 위치 고정**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_WINDOW\_SPLIT\_HORZ\_FIX (4335)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(4335);

#### \[VBScript\]

> editor.ExecuteCommandByID 4335
