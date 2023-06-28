# EE\_SET\_SEL\_LENGTH

선택 영역의 문자 길이를 변경합니다. 이 메시지를 명시적으로 보내거나
[Editor\_SetSelLength](../macro/editor_setsellength) 인라인 함수를 사용할 수
있습니다.

EE\_SET\_SEL\_LENGTH

wParam = (WPARAM) (UINT) nLen;

lParam = 0;

## 매개 변수

_nLen_

> 선택 영역의 문자 길이를 지정합니다. 반환은 항상 2 문자 길이 입니다(CR+LF).

## 반환 값

> 반환 값이 사용되지 않습니다.