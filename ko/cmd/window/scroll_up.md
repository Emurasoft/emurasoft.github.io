# 줄 스크롤 위로 명령

## 요약

한 줄 위로 문서를 스크롤합니다.

## 설명

한 줄 위로 문서를 스크롤합니다. 하지만, 구성 속성 대화 상자 [**스크롤** 탭](../../dlg/properties/scroll/index) 의 **이중선 스크롤** 체크 박스가 체크되어 있다면 두 줄로 스크롤합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **창** \> **스크롤** \> **줄 위로**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+UP ARROW

## 플러그인 명령 ID

```
EEID_SCROLL_UP (4170)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4170);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4170
```
