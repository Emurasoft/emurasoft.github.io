# 가로 분할 설정/해제 명령

### 요약

> 창 가로 분할을 설정/해제 합니다.

### 설명

> 현재 창이 세로로 분할되어 있거나 분할되어 있지 않은 경우, 이 명령은 현재 창을
> 수평한 창으로 분할하고, 즉시 창의 중앙에 분할 위치를 고정합니다.
> 현재 창이 이미 수평으로 분할되어 있는 경우, 이 명령은 현재 창으로부터 수평 분할을 제거합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **창** \> **분할** \> **가로 분할 설정/해제**
- 도구 모음: ![](../../images/windowsplithorzfix.gif)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL + -

### 플러그인 명령 ID

- EEID\_WINDOW\_SPLIT\_HORZ\_TOGGLE (4385)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(4385);

#### \[VBScript\]

> editor.ExecuteCommandByID 4385