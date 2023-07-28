# 따옴표 내 붙여넣기 명령

## 요약

따옴표 내에 클립보드의 내용을 붙여 넣습니다.

## 설명

커서 위치에 따옴표 내 클립보드의 내용을 붙여 넣습니다.
이 명령 이전에 [**복사** 명령](edit_copy) 또는
[**자르기** 명령](edit_cut) 을 사용하여 텍스트를 클립보드로 이동합니다.
이 명령은 속성 대화 상자의 [**일반** 탭](../../dlg/properties/general/index) 의 **항상 ANSI로 붙여 넣기** 체크 박스가 체크되어 있다면 [**시스템 기본 인코딩**](../../glossary/systemdefaultencoding) 을 사용하고,
체크되어 있지 않다면 유니코드를 사용합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **붙여넣기**
\> **따옴표 내 붙여넣기**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+B

## 플러그인 명령 ID

```
EEID_PASTE_PREFIX (4132)```

## 매크로

### \[JavaScript\]

```
document.selection.Paste(eeCopyQuotes);
```

### \[VBScript\]

```
document.selection.Paste eeCopyQuotes
```
