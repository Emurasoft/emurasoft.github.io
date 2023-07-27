# Editor\_ToolbarShow

사용자 지정 도구 모음을 보이거나 숨깁니다. 이 인라인 함수를 사용하거나 [EE\_TOOLBAR\_SHOW](../message/ee_toolbar_show)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_ToolbarShow( HWND hwnd, UINT nCustomRebarID, BOOL bVisible );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nToolbarID_

닫을 도구 모음을 지정합니다.EE\_TOOLBAR\_OPEN 메시지로부터의 반환 값입니다.

_bVisible_

도구 모음이 보여야 한다면 TRUE를 지정하고, 도구 모음이 숨겨져야 한다면 FALSE를 지정합니다.

## 반환 값

메시지가 성공하고 도구 모음 상태가 변경된 경우, 반환 값은 TRUE입니다. 메시지가 실패하고 도구 모음 상태가 변경되지 않은 경우, 반환 값은 FALSE입니다.

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
