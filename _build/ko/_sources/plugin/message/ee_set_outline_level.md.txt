# EE\_SET\_OUTLINE\_LEVEL

지정된 논리 줄에 대한 개요 수준을 설정합니다. 이 메시지를 명시적으로 보내거나 [Editor\_SetOutlineLevel](../macro/editor_setoutlinelevel) 인라인 함수를
사용할 수 있습니다.

EE\_SET\_OUTLINE\_LEVEL

wParam = (WPARAM) (INT\_PTR) nLogicalLine;

lParam = (LPARAM) (int) nLevel;

## 매개 변수

_nLogicalLine_

> 논리 줄을 지정합니다.

_nLevel_

> 개요 수준을 지정합니다.

## 반환 값

> 반환 값은 지정된 논리 줄의 이전 개요 수준입니다. 오류가 발생하는 경우, 반환 값은 -1입니다.

## 버전

> 엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.