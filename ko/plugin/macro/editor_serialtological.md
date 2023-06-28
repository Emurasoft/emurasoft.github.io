# Editor\_SerialToLogical

일련 위치를 논리 좌표로 변환합니다. 일련 위치는 전체 텍스트의 시작에서부터 0으로 시작하는 문자 인덱스입니다.
이 인라인 함수를 사용하거나
[EE\_SERIAL\_TO\_LOGICAL](../message/ee_serial_to_logical)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_SerialToLogical( HWND hwnd, UINT nSerial, POINT\_PTR\* pptLogical );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nSerial_

> 변환될 일련 위치를 지정합니다.

_pptLogical_

> 변환된 논리 좌표를 수신 할 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

## 반환 값

> 일련 위치를 반환합니다.