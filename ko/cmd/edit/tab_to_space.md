# 문서 탭 해제 명령

### 요약

> 전체 문서에서 탭을 공백으로 변환합니다.

### 설명

> 전체 문서의 모든 행의 시작점에 있는 탭을 공백으로 변환합니다.
> 탭의 공백 수는 [**탭/들여쓰기** 대화 상자](../../dlg/properties/general/indent/index) 에서
> 설정 가능합니다. 이 명령은 전체 문서 선택 후 [**탭 해제** 명령](untabify) 과 동일하게 작용되지만, 이 명령은 선택 영역을 확장하지 않습니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **고급** \> **문서 탭 해제**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL + SHIFT + T

### 플러그인 명령 ID

- EEID\_TAB\_TO\_SPACE (4253)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(4253);

#### \[VBScript\]

> editor.ExecuteCommandByID 4253
