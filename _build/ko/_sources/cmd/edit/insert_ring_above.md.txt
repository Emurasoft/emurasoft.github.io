# Ring 발음 구별 부호 명령

### 요약

> Ring 발음 구별 부호로 문자를 삽입합니다.

### 설명

> 이 명령을 선택한 후에 a 또는 A를 입력하면 커서 위치에 Ring 발음 구별 부호 문자 (å 또는 Å)가 삽입되며, 공백을 입력하면 (°)를 삽입합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **삽입**
\> **강조 표시/ 특수 문자 삽입** \> **Ring 발음 구별 부호**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+2

### 플러그인 명령 ID

- EEID\_INSERT\_RING\_ABOVE (4308)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(4308);

#### \[VBScript\]

> editor.ExecuteCommandByID 4308