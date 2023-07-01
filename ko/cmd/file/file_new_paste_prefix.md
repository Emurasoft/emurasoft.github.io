# 새로 만들기 후 따옴표 내 붙여넣기 명령

### 요약

> 새 파일을 생성하고 클립보드의 내용을 따옴표 내 붙여넣습니다.

### 설명

> 이 명령은 [**새 텍스트** \
> 명령](file_new) 후에 [**따옴표 내 붙여넣기** 명령](../edit/paste_prefix) 적용과
> 동일하게 해당됩니다. 새 파일은 기본적으로 텍스트 구성을 사용합니다. [**구성 정의** 대화 상자](../../dlg/configurations/index) 에서 기본 구성을 변경할 수 있습니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **새로 만들기** \> **새로 만들기 후 따옴표 내 붙여넣기**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_NEW\_PASTE\_PREFIX (4271)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(4271);

#### \[VBScript\]

> editor.ExecuteCommandByID 4271
