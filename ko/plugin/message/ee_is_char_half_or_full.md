# EE\_IS\_CHAR\_HALF\_OR\_FULL

지정된 문자가 반자인지 전자인지 여부를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_IsCharHalfOrFull](../macro/editor_ischarhalforfull) 인라인 함수를 사용할 수 있습니다.

EE\_IS\_CHAR\_HALF\_OR\_FULL

wParam = (WPARAM)(WCHAR)ch;

lParam = (LPARAM)0;

## 매개 변수

_ch_

검색된 유니코드에 의한 문자 조합을 지정합니다.

## 반환 값

문자가 전자 문자인 경우, 반환 값은 2입니다. 문자가 반자 문자인 경우, 반환 값은 1입니다.
