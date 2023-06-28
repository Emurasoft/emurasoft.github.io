# Editor\_SetOutlineArray

지정된 여러 줄에 대한 개요 수준을 설정합니다. 이 인라인 함수를 사용하거나
[EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetOutlineArray( HWND hwnd, INT\_PTR nStartLine, INT\_PTR nCount, BYTE\* pLevelData );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nStartLine_

> 다중 선의 첫번째 선을 지정합니다.

_nCount_

> 다중 선의 번호를 지정합니다.

_pLevelData_

> 개요 수준을 지정하는 BYTE의 배열을 지정합니다.

## 반환 값

> 변경 사항이 없는 경우 반환 값은 FALSE입니다. 그렇지 않으면, 반환 값은 TRUE입니다.

## 버전

> EmEditor 버전 13 이상에서만 지원됩니다.