# Editor\_DocGetLines

지정된 문서를 위한 줄의 수를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_LINES](../message/ee_get_lines) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetLines( HWND hwnd, int iDoc, int nLogical );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_iDoc_

대상 문서의 인덱스를 지정합니다.-1이 지정된 경우, 현재 활성화 중인 문서가 대상으로 지정됩니다.

_nLogical_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
|값 |의미 |
| POS\_VIEW | 좌표를 표시합니다. |
| POS\_LOGICAL\_A | 논리 좌표(더블 바이트 문자를 2로 계산) |
| POS\_LOGICAL\_W | 논리 좌표(더블 바이트 문자를 1로 계산) |

## 반환 값

EmEditor 내 줄의 수를 반환합니다. 마지막 줄이 반환과 함께 끝나는 경우, 마지막 줄도 계산됩니다.
텍스트가 비어있는 경우, 1이 반환됩니다.
