# LF 만 명령

### 요약

> 현재 커서 위치에 LF를 삽입합니다.

### 설명

> 현재 커서 위치에 line feed (LF)를 삽입합니다. 엠에디터는 새로운 행으로써 CR과 LF의 혼합을 파일 편집에 사용 할 수 있습니다.
> Enter키를 누르면 현재 행과 같은 새로운 라인 입력 방법 (CR만, LF만, 또는 CR+LF)으로 삽입됩니다.
> 이 명령은 현재 행에 어떤 새로운 라인 방법이 사용 되었는지에 관계 없이 항상 LF만을 삽입합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **삽입**
\> **LF 만**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_INSERT\_LF (4146)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(4146);

#### \[VBScript\]

> editor.ExecuteCommandByID 4146
