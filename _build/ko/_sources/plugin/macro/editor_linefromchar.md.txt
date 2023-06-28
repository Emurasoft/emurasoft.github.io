# Editor\_LineFromChar

지정된 문자 인덱스를 포함한 줄의 인덱스를 검색합니다 (일련 위치). 문자 인덱스는 전체 텍스트의 시작으로부터의 문자의 0으로 시작하는
인덱스입니다. 이 인라인 함수를 사용하거나
[EE\_LINE\_FROM\_CHAR](../message/ee_line_from_char)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_LineFromChar( HWND hwnd, int nLogical, UINT nSerialIndex );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nLogical_

> 다음의 값들 중 하나를 지정합니다.
>
> |     |     |
> | --- | --- |
> | **값** | **의미** |
> | POS\_VIEW | 좌표를 표시합니다. |
> | POS\_LOGICAL\_A | 논리 좌표(더블 바이트 문자를 2로 계산) |
> | POS\_LOGICAL\_W | 논리 좌표(더블 바이트 문자를 1로 계산) |

_nSerialIndex_

> 검색된 번호의 줄에 포함된 문자의 문자 인덱스를 지정합니다.
> 이 매개 변수가 -1인 경우, EE\_LINE\_FROM\_CHAR는 현재 줄 (커서를 포함한 줄)의 줄 번호를 검색합니다.

## 반환 값

> 반환 값은 _nSerialIndex_ 에 의해 지정된 문자 인덱스를 포함하는 줄의 0으로 시작하는 줄 번호입니다.