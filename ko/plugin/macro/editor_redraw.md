# Editor\_Redraw

다시 그리려는 EmEditor의 변경을 허락하거나 다시 그리려는 EmEditor의 변경을 막습니다. 이 인라인 함수를 사용하거나
[EE\_REDRAW](../message/ee_redraw) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_Redraw( HWND hwnd, BOOL bRedraw );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_bRedraw_

> 다시 그리기 상태를 지정합니다. 매개 변수가 TRUE인 경우, 내용은 변경 후 다시 그려질 수 있습니다.
> 매개 변수가 FALSE인 경우, 내용은 변경 후 다시 그리기 할 수 없습니다.

## 반환 값

> 반환 값이 사용되지 않습니다.
