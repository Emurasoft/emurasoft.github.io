# 매칭 태그 확장 명령

### 요약

> 매칭하는 태그까지 선택을 확장합니다.

### 설명

> 이 명령은 XML 또는 XHTML 문서안에 커서가 여는/닫히는 태그에 위치 해 있다면, 대응하는 닫히는/여는 태그까지 선택을 확장합니다.

### 실행하는 방법

- 기본 메뉴: **편집** \> **고급** \> **현재 태그 선택**
- [모든 명령](../tools/all_commands): **편집** \> **선택 확장** \> **매칭 태그 확장**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+.

### 플러그인 명령 ID

- EEID\_SHIFT\_NEXT\_TAG (4602)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(4602);

#### \[VBScript\]

> editor.ExecuteCommandByID 4602
