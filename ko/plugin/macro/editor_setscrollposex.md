# Editor\_SetScrollPosEx

스크롤 바 위치를 지정합니다. 이 인라인 함수를 사용하거나 [EE\_SET\_SCROLL\_POS](../message/ee_set_scroll_pos) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetScrollPos( HWND hwnd, POINT\* pptPos, BOOL bCanMoveCursor );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pptPos_

스크롤 바 위치를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.
커서 위치는 변경되지 않습니다.

_bCanMoveCursor_

매개변수가 TRUE이고 [**스크롤링으로 커서 이동** 체크 박스](../../dlg/properties/scroll/index) 가
선택된 경우, 커서 위치 또한 이동합니다. 매개 변수가 FALSE인 경우, 커서 위치는 이동하지 않습니다.

## 반환 값

반환 값이 사용되지 않습니다.

## 버전

엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.
