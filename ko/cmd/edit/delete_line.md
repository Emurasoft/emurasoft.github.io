# 줄 삭제 명령

### 요약

> 현재 줄을 삭제합니다.

### 설명

> 커서 위치의 논리 줄을 삭제합니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **삭제** \> **줄 삭제**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+L

### 플러그인 명령 ID

- EEID\_DELETE\_LINE (4190)

### 매크로

#### \[JavaScript\]

> document.selection.SelectLine();
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.SelectLine
>
> document.selection.Delete 1
