# EE\_SET\_OUTLINE\_ARRAY

지정된 여러 줄에 대한 개요 수준을 설정합니다. 이 메시지를 명시적으로 보내거나
[Editor\_SetOutlineArray](../macro/editor_setoutlinearray) 인라인 함수를
사용할 수 있습니다.

EE\_SET\_OUTLINE\_ARRAY

wParam = (WPARAM) 0;

lParam = (LPARAM) (OUTLINE\_ARRAY\_INFO\*) pOutlineArrayInfo;

## 매개 변수

_pOutlineArrayInfo_

[OUTLINE\_ARRAY\_INFO](../structure/outline_array_info) 구조에 대한 포인터입니다.

## 반환 값

변경 사항이 없는 경우 반환 값은 FALSE 입니다. 그렇지 않으면, 반환 값은 TRUE 입니다.

## 버전

EmEditor 버전 13 이상에서만 지원됩니다.
