# Editor\_SetOutlineLevel

지정된 논리 줄에 대한 개요 수준을 설정합니다. 이 인라인 함수를 사용하거나 [EE\_SET\_OUTLINE\_LEVEL](../message/ee_set_outline_level) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine, int nLevel );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nLogicalLine_

> 논리 줄을 지정합니다.

_nLevel_

> 개요 수준을 지정합니다.

## 반환 값

> 반환 값은 지정된 논리 줄의 이전 개요 수준입니다. 오류가 발생하는 경우, 반환 값은 -1입니다.

## 버전

> 엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.
