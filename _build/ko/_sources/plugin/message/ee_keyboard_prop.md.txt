# EE\_KEYBOARD\_PROP

지정된 command ID와 구성을 위한 키보드 속성을 표시합니다. 이 메시지를 명시적으로 보내거나
[Editor\_KeyboardProp](../macro/editor_keyboardprop) 인라인 함수를 사용할 수
있습니다.

EE\_KEYBOARD\_PROP

wParam = (WPARAM)(UINT)nCmdID;

lParam = (LPARAM)(LPCWSTR)pszConfigName;

## 매개 변수

_nCmdID_

> 키보드 속성에 초기 선택의 command ID를 지정합니다.

_pszConfigName_

> EmEditor가 키보드 속성을 표시하는 구성을 지정합니다.

## 반환 값

> 사용자가 구성 속성에서 OK를 선택한 경우, 반환 값은 TRUE입니다.
> 사용자가 취소를 선택한 경우, 반환 값은 FALSE입니다.