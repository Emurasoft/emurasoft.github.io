# Editor\_KeyboardProp

지정된 command ID와 구성을 위한 키보드 속성을 표시합니다. 이 인라인 함수를 사용하거나 [EE\_KEYBOARD\_PROP](../message/ee_keyboard_prop) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_KeyboardProp( HWND hwnd, UINT nCmdID, LPCWSTR pszConfigName );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nCmdID_

> 키보드 속성에 초기 선택의 command ID를 지정합니다.

_pszConfigName_

> EmEditor가 키보드 속성을 표시하는 구성을 지정합니다.

## 반환 값

> 사용자가 구성 속성에서 OK를 선택한 경우, 반환 값은 TRUE입니다.
> 사용자가 취소를 선택한 경우, 반환 값은 FALSE입니다.