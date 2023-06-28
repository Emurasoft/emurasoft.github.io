# 시스템 기본 인코딩으로 붙여넣기 명령

### 요약

> [시스템 기본 인코딩](../../glossary/index) 으로 클립보드의 내용을 붙여 넣습니다.

### 설명

> 커서 위치에서 [시스템 기본 인코딩](../../glossary/index) 으로 클립보드의 내용을 붙여 넣습니다.
> 이 명령 사전에, 텍스트를 클립보드에 넣기 위해 [**복사** 명령](edit_copy) 또는 [**자르기** 명령](edit_cut) 을 사용합니다.
> 이 명령은 속성 대화 상자의 [**일반** 탭](../../dlg/properties/general/index) 의 **항상 ANSI로 붙여 넣기** 체크 박스가 체크되어 있다면 [**붙여넣기** 명령](edit_paste) 과 동일하게 작용됩니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **붙여넣기**
\> **시스템 기본 인코딩으로 붙여넣기**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: ALT+CTRL+V

### 플러그인 명령 ID

- EEID\_EDIT\_PASTE\_ANSI (4262)

### 매크로

#### \[JavaScript\]

> document.selection.Paste(eeCopySystemDefault);

#### \[VBScript\]

> document.selection.Paste eeCopySystemDefault