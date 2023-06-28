# Editor\_SetSelView

선택 영역의 시작 위치와 끝 위치를 변경합니다. 이 인라인 함수를 사용하거나 [EE\_SET\_SEL\_VIEW](../message/ee_set_sel_view) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetSelView( HWND hwnd, POINT\_PTR\* pptSelStart, POINT\_PTR\* pptSelEnd );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pptSelStart_

> 선택 영역의 시작 위치를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

_pptSelEnd_

> 선택 영역의 끝 위치를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

## 반환 값

> 반환 값이 사용되지 않습니다.