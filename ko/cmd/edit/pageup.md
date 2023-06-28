# 페이지 위로 명령

### 요약

> 한 페이지 위로 커서를 이동합니다.

### 설명

> 한 페이지 위로 커서를 이동합니다. 구성 속성 대화 상자 [**스크롤** 탭](../../dlg/properties/scroll/index) 의 **1/2 페이지 스크롤** 체크 박스가 체크되어 있다면, 커서가 페이지의 절반만 이동하게 됩니다.

### 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **세로로 커서 이동** \> **페이지 위로**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: PAGE UP

### 플러그인 명령 ID

- EEID\_PAGEUP (4162)

### 매크로

#### \[JavaScript\]

> document.selection.PageUp(false,1);

#### \[VBScript\]

> document.selection.PageUp false,1