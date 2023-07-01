# 줄 나누기 명령

### 요약

> 새 줄을 삽입하고 후행 공백을 제거하여 선을 나눕니다.

### 설명

> 새 줄을 삽입하고 후행 공백을 제거하여 선을 나눕니다.
> [**새 행 삽입** 명령](insert_cr_wrap) 과 비슷하지만, 이 명령은 새로운 행 이전에 각 행의 공백을 제거합니다.
> 새 행 방법은 현재 행에서 사용되는 방법과 일치합니다.

### 실행하는 방법

- 기본 메뉴: **편집** \> **선택 변환** \> **줄 나누기**
- [모든 명령](../tools/all_commands): **편집** \> **선택 변환** > **줄 나누기**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_SPLIT\_LINES (4379)

### 매크로

#### \[JavaScript\]

> document.selection.Format(eeFormatSplitLines);

#### \[VBScript\]

> document.selection.Format eeFormatSplitLines
