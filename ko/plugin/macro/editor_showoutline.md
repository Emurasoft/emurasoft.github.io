# Editor\_ShowOutline

개요를 보이거나 숨깁니다. 이 인라인 함수를 사용하거나 [EE\_SHOW\_OUTLINE](../message/ee_show_outline) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_ShowOutline( HWND hwnd, WPARAM nFlags );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nFlags_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| **값** | **의미** |
| SHOW\_OUTLINE\_SHOW | 개요를 보입니다. |
| SHOW\_OUTLINE\_HIDE | 개요를 숨깁니다. |

## 반환 값

반환 값이 사용되지 않습니다.

## 버전

엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.
