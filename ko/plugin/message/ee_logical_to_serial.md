# EE\_LOGICAL\_TO\_SERIAL

논리 좌표를 일련 위치로 변환합니다.
일련 위치는 전체 텍스트의 시작으로부터의 0으로 시작하는 문자 인덱스 입니다.
이 메시지를 명시적으로 보내거나
[Editor\_LogicalToSerial](../macro/editor_logicaltoserial) 인라인 함수를
사용할 수 있습니다.

EE\_LOGICAL\_TO\_SERIAL

wParam = 0;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical

## 매개 변수

_pptLogical_

변환될 논리 좌표를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

## 반환 값

일련 위치를 반환합니다.
