# Editor\_SetCaretPosEx

커서 위치를 이동하고 필요에 따라 선택 영역을 확장합니다. 이 인라인 함수를 사용하거나 [EE\_SET\_CARET\_POS](../message/ee_set_caret_pos) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetCaretPosEx( HWND hwnd, int nLogical, POINT\_PTR\* pptPos,
BOOL bExtend );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nLogical_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| **값** | **의미** |
| POS\_VIEW | 좌표를 표시합니다. |
| POS\_LOGICAL\_A | 논리 좌표(더블 바이트 문자를 2로 계산) |
| POS\_LOGICAL\_W | 논리 좌표(더블 바이트 문자를 1로 계산) |
| POS\_SCROLL\_ALWAYS | POS\_SCROLL\_CENTER 또는 POS\_SCROLL\_TOP과 함께 사용될 때, 현재 커서 위치가 이미 보일지라도 커서 위치가 이동합니다. |
| POS\_SCROLL\_CENTER | 커서 위치가 창의 중앙에 가깝게 됩니다. |
| POS\_SCROLL\_DONT\_CARE | 커서 위치가 스크롤이 최소화 된 곳에 위치하게 됩니다. |
| POS\_SCROLL\_TOP | 커서 위치가 창의 상단에 위치하게 됩니다. |

_pptPos_

커서 위치를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터 입니다.

_bExtend_

현재 선택 영역을 확장할 지 여부를 결정합니다. _bExtend_ 가 TRUE인 경우,
기준 위치의 끝이 있던 곳에 남아 있는 동안 활성화된 선택 영역의 끝이 위치로 이동합니다.
그렇지 않으면, 양 끝이 모두 지정된 위치로 이동합니다.

## 반환 값

반환 값이 사용되지 않습니다.

## 버전

EmEditor 버전 4.03 이상에서만 지원됩니다. 하지만, POS\_SCROLL\_DONT\_CARE,
POS\_SCROLL\_CENTER, 및 POS\_SCROLL\_TOP flag는 EmEditor 버전 6 이상에서만 지원됩니다.POS\_SCROLL\_ALWAYS는
EmEditor 버전 7.00.4 이상에서만 지원됩니다.
