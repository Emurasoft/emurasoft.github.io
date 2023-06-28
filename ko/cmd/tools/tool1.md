# 도구 목록 명령

### 요약

> 지정된 도구를 시작합니다 (여러 항목).

### 설명

> 이 명령은 여러 메뉴 항목을 포함하고 있습니다.
> 이 명령은 지정된 도구를 시작합니다.
> 사용 가능한 도구는 [**외부 도구** 대화 상자](../../dlg/tools/index) 에
> 정의되어 있습니다.

### 실행하는 방법

- 기본 메뉴: **도구** \> **외부 도구** \> ( **도구 이름**)
- [모든 명령](all_commands): **외부 도구**
\> ( **도구 이름**)
- 도구 모음: 도구 도구 모음의 각 버튼
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- From EEID\_TOOL1 through EEID\_TOOL1 + 255 (from 8192 through 8192 + 255)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(8192+i);  // i is an integer from 0 through
> 255

#### \[VBScript\]

> editor.ExecuteCommandByID 8192+i  ' i is an integer from 0 through 255