# EE\_SET\_SEL\_VIEW

선택 영역의 시작 위치와 끝 위치를 변경합니다. 이 메시지를 명시적으로 보내거나
[Editor\_SetSelView](../macro/editor_setselview) 인라인 함수를 사용할 수
있습니다.

EE\_SET\_SEL\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptSelStart;

lParam = (LPARAM) (POINT\_PTR\*) pptSelEnd;

## 매개 변수

_pptSelStart_

> 선택 영역의 시작 위치를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

_pptSelEnd_

> 선택 영역의 끝 위치를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

## 반환 값

> 반환 값이 사용되지 않습니다.
