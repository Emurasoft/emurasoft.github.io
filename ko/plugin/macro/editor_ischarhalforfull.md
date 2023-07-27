# Editor\_IsCharHalfOrFull

지정된 문자가 반자인지 전자인지 여부를 검색합니다. 이 인라인 함수를 사용하거나
[EE\_IS\_CHAR\_HALF\_OR\_FULL](../message/ee_is_char_half_or_full) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_IsCharHalfOrFull( HWND hwnd, WCHAR ch );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_ch_

검색된 유니코드에 의한 문자 조합을 지정합니다.

## 반환 값

문자가 전자 문자인 경우, 반환 값은 2입니다. 문자가 반자 문자인 경우, 반환 값은 1입니다.
