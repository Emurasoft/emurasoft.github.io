# EE\_GET\_LINES

EmEditor에서 줄 수를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_DocGetLines](../macro/editor_docgetlines) 인라인 함수 또는 [Editor\_GetLines](../macro/editor_getlines) 인라인 함수를 사용 할 수 있습니다.

EE\_GET\_LINES

wParam = (WPARAM) MAKEWPARAM(nLogical, iDoc+1);

lParam = 0;

## 매개 변수

_nLogical_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| **값** | **의미** |
| POS\_VIEW | 좌표를 표시합니다. |
| POS\_LOGICAL\_A | 논리 좌표(더블 바이트 문자를 2로 계산) |
| POS\_LOGICAL\_W | 논리 좌표(더블 바이트 문자를 1로 계산) |

_iDoc_

대상 문서의 인덱스를 지정합니다.
1로 시작하는 인덱스는 wParam의 상위 단어에 지정되어야 합니다.
wParam의 상위 단어에 0이 지정되면, 현재 활성화 중인 문서가 대상으로 지정됩니다.

## 반환 값

EmEditor 내 줄의 수를 반환합니다. 마지막 줄이 반환과 함께 끝나는 경우, 마지막 줄도 계산됩니다.
텍스트가 비어있는 경우, 1이 반환됩니다.
