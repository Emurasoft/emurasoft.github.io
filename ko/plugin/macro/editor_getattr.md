# Editor\_GetAttr

클립보드 기록의 지정된 위치에 텍스트를 제거합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_ATTR](../message/ee_get_attr)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetAttr( HWND hwnd, ATTR\_INFO\* pAI );

## 매개 변수

_pAI_

> [ATTR\_INFO](../structure/attr_info) 구조에 대한 포인터 입니다.

## 반환 값

> 반환 값은 성공할 시 TRUE이고, 실패 시 FALSE입니다.

## 버전

> EmEditor 버전 9 이상에서만 지원됩니다.