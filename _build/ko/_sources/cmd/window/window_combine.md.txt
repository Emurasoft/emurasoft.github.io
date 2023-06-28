# 탭 활성화 명령

### 요약

> 모든 창을 결합하기 위해 탭을 활성화 하거나 분리하기 위해 탭을 비활성화 합니다.

### 설명

> 비활성화 되있는 경우 탭을 활성화하고, 이미 활성화된 경우 탭을 비활성화 합니다.
> 탭이 활성화되었을 때, 현재 열려있는 모든 문서들은 창의 상단의 탭 메뉴에 표시됩니다.
> 하나의 엠에디터 아이콘만이 윈도우 작업 표시 줄에 표시됩니다.

### 실행하는 방법

- 기본 메뉴: **창** \> **탭 활성화**
- [모든 명령](../tools/all_commands): **창** \> **탭 활성화** \> **탭 활성화**
- 도구 모음: ![](../../images/windowcombine.gif)
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_WINDOW\_COMBINE (4342)

### 매크로

#### \[JavaScript\]

> editor.EnableTab = !editor.EnableTab;

#### \[VBScript\]

> editor.EnableTab = Not editor.EnableTab