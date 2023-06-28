# 줄 합치기 명령

### 요약

> 새 줄을 제거하고 각 줄의 끝에 공백을 삽입하여 줄을 합칩니다.

### 설명

> 새 줄을 제거하고 각 줄의 끝에 공백을 삽입하여 줄을 합칩니다.
> [**새 행 제거** 명령](delete_cr_wrap) 과 비슷하지만, 이 명령은 줄 바꿈 위치의 각 행에 공백을 삽입합니다.

### 실행하는 방법

- 기본 메뉴: **편집** > **선택 변환** \> **줄 합치기**
- [모든 명령](../tools/all_commands): **편집** \> **선택 변환** \> **줄 합치기**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_JOIN\_LINES (4378)

### 매크로

#### \[JavaScript\]

> document.selection.Format(eeFormatJoinLines);

#### \[VBScript\]

> document.selection.Format eeFormatJoinLines