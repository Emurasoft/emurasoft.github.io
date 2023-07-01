# Editor\_LineIndex

EmEditor에서 지정된 줄의 첫 문자의 문자 인덱스를 검색합니다. 문자 인덱스는 컨트롤 편집의 시작으로부터의 문자의 0으로 시작하는
인덱스 입니다. 이 인라인 함수를 사용하거나 [EE\_LINE\_INDEX](../message/ee_line_index)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_LineIndex( HWND hwnd, BOOL bLogical, int yLine );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_bLogical_

> 논리 좌표에 의한 줄 번호인 경우 TRUE를 지정합니다.
> 표시 좌표에 의한 줄 번호인 경우에는 FALSE를 지정합니다.

_yLine_

> 0으로 시작하는 줄 번호를 지정합니다. -1의 값은 현재 줄 번호 (커서를 포함하는 줄)를 지정합니다.

## 반환 값

> 반환 값은 _yLine_ 매개 변수에 지정된 줄의 문자 인덱스입니다.
