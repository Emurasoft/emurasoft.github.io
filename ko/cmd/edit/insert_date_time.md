# 날짜 및 시간 명령

### 요약

> 날짜 및 시간을 삽입합니다.

### 설명

> 커서 위치에 현재 날짜 및 시간를 삽입합니다. 이 명령은 날짜, 공백, 시간 순으로 삽입합니다.
> 시간과 날짜에 사용되는 형식은 Windows에서 **제어판** 의 **국가 및 언어 옵션** 을 선택 한 후 **날짜 및 시간** 을 선택하여
> 구성 할 수 있습니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **삽입**
\> **날짜 및 시간**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: SHIFT+F5

### 플러그인 명령 ID

- EEID\_INSERT\_DATE\_TIME (4138)

### 매크로

#### \[JavaScript\]

> document.selection.InsertDate(eeDateDateTime);

#### \[VBScript\]

> document.selection.InsertDate eeDateDateTime