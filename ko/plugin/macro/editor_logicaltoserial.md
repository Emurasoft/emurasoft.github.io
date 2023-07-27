# Editor\_LogicalToSerial

논리 좌표를 일련 위치로 변환합니다. 일련 위치는 전체 텍스트의 시작으로부터의 0으로 시작하는 문자 인덱스 입니다.
이 인라인 함수를 사용하거나
[EE\_LOGICAL\_TO\_SERIAL](../message/ee_logical_to_serial)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_LogicalToSerial( HWND hwnd, POINT\_PTR\* pptLogical );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pptLogical_

변환될 논리 좌표를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

## 반환 값

일련 위치를 반환합니다.
