# Editor\_GetMargin

여백 크기를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_MARGIN](../message/ee_get_margin)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_Convert( HWND hwnd );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

## 반환 값

현재 선택된 여백 크기를 반환합니다. 일반 줄의 여백 크기와 인용줄의 여백 크기가 다른 경우,
더 큰 여백이 반환됩니다. 줄이 창 크기에 의해 줄 바꿈 된 경우, 반환 값은 현재 창 크기에 의해 결정됩니다.
