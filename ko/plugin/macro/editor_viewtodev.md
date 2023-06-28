# Editor\_ViewToDev

지정된 위치의 표시 좌표를 장치 (클라이언트) 좌표로 변환합니다. 이 인라인 함수를 사용하거나
[EE\_VIEW\_TO\_DEV](../message/ee_view_to_dev) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_ViewToDev( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptDev );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pptView_

> 변환 될 표시 좌표를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터 입니다.

_pptDev_

> 변환 된 장치 좌표를 수신 할 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터 입니다.

## 반환 값

> 반환 값이 사용되지 않습니다.