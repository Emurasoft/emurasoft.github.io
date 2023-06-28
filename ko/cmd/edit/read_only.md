# 읽기 전용 명령

### 요약

> 현재 파일을 읽기 전용 상태로 전환합니다.

### 설명

> 파일의 변경 내용을 저장하는 기능을 활성화하거나 비활성화 합니다.

### 실행하는 방법

- 기본 메뉴: **편집** \> **읽기 전용**
- [모든 명령](../tools/all_commands): **편집** \> **고급**
\> **읽기 전용**
- 도구 모음: 없음
- 상태 표시줄: **읽기** 를 두 번 클릭
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_READ\_ONLY (4113)

### 매크로

#### \[JavaScript\]

> document.ReadOnly=true;

or

> document.ReadOnly=false;

#### \[VBScript\]

> document.ReadOnly=true

or

> document.ReadOnly=false