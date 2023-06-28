# 붙여넣기 명령

### 요약

> 클립보드의 내용을 커서위치에 붙여 넣습니다.

### 설명

> 클립보드의 내용을 커서위치에 붙여 넣습니다. 이 명령 이전에 [**복사** 명령](edit_copy) 또는
> [**자르기** 명령](edit_cut) 을 사용하여 텍스트를 클립보드로 이동합니다.
> 이 명령은 속성 대화 상자의 [**일반** 탭](../../dlg/properties/general/index) 의 **항상 ANSI로 붙여 넣기** 체크 박스가 체크되어 있다면 [**시스템 기본 인코딩**](../../glossary/systemdefaultencoding) 을 사용하고,
> 체크되어 있지 않다면 유니코드를 사용합니다.

### 실행하는 방법

- 기본 메뉴: **편집** \> **붙여넣기**
- [모든 명령](../tools/all_commands): **편집** \> **붙여넣기**
\> **붙여넣기**
- 도구 모음: ![](../../images/paste.gif)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+V 또는 Shift+Insert

### 플러그인 명령 ID

- EEID\_EDIT\_PASTE (4129)

### 매크로

#### \[JavaScript\]

> document.selection.Paste(eeCopyUnicode);

#### \[VBScript\]

> document.selection.Paste eeCopyUnicode