# EE\_GET\_SCROLL\_POS

스크롤 바의 현재 위치를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetScrollPos](../macro/editor_getscrollpos) 인라인 함수를 사용할 수 있습니다.

EE\_GET\_SCROLL\_POS

wParam = 0;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## 매개 변수

_pptPos_

> 스크롤 바 위치를 수신 할 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

## 반환 값

> 반환 값이 사용되지 않습니다.