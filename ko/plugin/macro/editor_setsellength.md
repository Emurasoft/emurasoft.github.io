# Editor\_SetSelLength

선택 영역의 문자 길이를 변경합니다. 이 인라인 함수를 사용하거나
[EE\_SET\_SEL\_LENGTH](../message/ee_set_sel_length)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetSelLength( HWND hwnd, UINT nLen );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nLen_

> 선택 영역의 문자 길이를 지정합니다.반환은 항상 2 문자 길이 입니다 (CR+LF).

## 반환 값

> 반환 값이 사용되지 않습니다.
