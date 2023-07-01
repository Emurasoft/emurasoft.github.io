# 첫 글자를 대문자로 명령

### 요약

> 선택 영역에서 각 단어의 첫 글자를 대문자로 변환합니다.

### 설명

> 선택 영역에서 각 단어의 첫 글자를 대문자로 변환하고 나머지 글자들을 소문자로 변환합니다.

### 실행하는 방법

- 기본 메뉴: **편집** \> **선택 변환** \> **첫 글자를 대문자로**
- [모든 명령](../tools/all_commands): **편집** \> **선택 변환** \> **첫 글자를 대문자로**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_CAPITALIZE (4381)

### 매크로

#### \[JavaScript\]

> document.selection.ChangeCase(eeCaseCapitalize);

#### \[VBScript\]

> document.selection.ChangeCase eeCaseCapitalize
