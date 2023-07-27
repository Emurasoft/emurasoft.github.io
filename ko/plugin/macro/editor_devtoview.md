# Editor\_DevToView

지정된 위치의 장치 (클라이언트) 좌표를 표시 좌표로 변환합니다. 이 인라인 함수를 사용하거나
[EE\_DEV\_TO\_VIEW](../message/ee_dev_to_view) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_DevToView( HWND hwnd, POINT\_PTR\* pptDev, POINT\_PTR\* pptView );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pptDev_

장치 좌표가 변환되도록 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한
포인터 입니다.

_pptView_

변환된 표시 좌표를 받기 위한 [POINT\_PTR 구조](../structure/point_ptr) 에
포인터입니다.

## 반환 값

반환 값이 사용되지 않습니다.
