# 새 파일, 따옴표 내 붙여넣기와 반환 명령

### 요약

> 새 파일을 생성하고 현재 선택 영역을 따옴표 내 붙여넣고 반환합니다.

### 설명

> 이 명령은 [**새 텍스트** \
> 명령](file_new) 후에 [**따옴표 내 붙여넣기와 반환** 명령](../edit/paste_prefix_return) 작용과 동일시 해당합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **새로 만들기** \> **새 파일, 따옴표 내 붙여넣기와 반환**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_NEW\_PASTE\_PREFIX\_RETURN (4272)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(4272);

#### \[VBScript\]

> editor.ExecuteCommandByID 4272