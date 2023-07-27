# EE\_GET\_REF

지정된 플러그 인의 참조 번호를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetRef](../macro/editor_getref) 인라인 함수를 사용할 수 있습니다.

EE\_GET\_REF

wParam = 0;

lParam = (LPARAM)(ATOM)atom;

## 매개 변수

_atom_

지정된 플러그 인 파일 이름의 atom을 지정합니다.

## 반환 값

반환 값은 지정된 플러그 인의 참조 번호입니다. 반환 값이 0인 경우, 지정된 플러그인은 EmEditor로부터
안전하게 언로드될 수 있습니다.
