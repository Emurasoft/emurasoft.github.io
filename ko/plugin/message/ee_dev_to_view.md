# EE\_DEV\_TO\_VIEW

C지정된 위치의 장치 (클라이언트) 좌표를 표시 좌표로 변환합니다. 이 메시지를 명시적으로 보내거나
[Editor\_DevToView](../macro/editor_devtoview) 인라인 함수를 사용할 수 있습니다.

EE\_DEV\_TO\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptDev;

lParam = (LPARAM) (POINT\_PTR\*) pptView;

## 매개 변수

_pptDev_

> 장치 좌표가 변환되도록 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터 입니다.

_pptView_

> 변환된 표시 좌표를 받기 위한 [POINT\_PTR 구조](../structure/point_ptr) 에 포인터입니다.

## 반환 값

> 반환 값이 사용되지 않습니다.