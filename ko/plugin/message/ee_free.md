# EE\_FREE

지정된 플러그 인을 해제합니다. 이 메시지를 명시적으로 또는
[Editor\_Free](../macro/editor_free) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_FREE

wParam = 0;

lParam = (LPARAM)(ATOM)atom;

## 매개 변수

_atom_

> 지정된 플러그 인 파일 이름의 atom을 지정합니다.

## 반환 값

> 플러그 인이 해제된 경우, 반환 값은 TRUE입니다.
> 플러그 인이 해제되지 않은 경우, 반환 값은 FALSE입니다.