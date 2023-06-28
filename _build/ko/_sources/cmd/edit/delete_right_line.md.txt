# 오른쪽 줄 삭제 명령

### 요약

> 커서의 오른쪽 줄을 삭제합니다.

### 설명

> 커서 위치에서 커서의 논리 줄 마지막 부분의 텍스트까지 삭제합니다.

### 실행하는 방법

- 기본 메뉴: **편집** \> **고급** \> **오른쪽 줄 삭제**
- [모든 명령](../tools/all_commands): **편집** \> **삭제** \> **오른쪽 줄 삭제**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- EEID\_DELETE\_RIGHT\_LINE (4191)

### 매크로

#### \[JavaScript\]

> document.selection.EndOfLine(true,eeLineLogical);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.EndOfLine true,eeLineLogical
>
> document.selection.Delete 1