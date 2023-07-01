# EE\_GET\_ANCHOR\_POS

선택 영역의 원점을 검색합니다. 이 메시지를 명시적으로 또는 [Editor\_GetAnchorPos](../macro/editor_getanchorpos) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_GET\_ANCHOR\_POS

wParam = (WPARAM) (int) nLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## 매개 변수

_nLogical_

> 다음의 값 중 하나를 지정합니다.
>
> |     |     |
> | --- | --- |
> | **값** | **의미** |
> | POS\_VIEW | 좌표를 표시합니다. |
> | POS\_LOGICAL\_A | 논리 좌표(더블 바이트 문자를 2로 계산) |
> | POS\_LOGICAL\_W | 논리 좌표(더블 바이트 문자를 1로 계산) |

_pptPos_

> 선택 영역의 원점을 수신할 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

## 반환 값

> 반환 값이 사용되지 않습니다.
