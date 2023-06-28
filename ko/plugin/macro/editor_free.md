# Editor\_Free

지정된 플러그 인을 해제합니다. 이 인라인 함수를 사용하거나 [EE\_FREE](../message/ee_free) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_Free( HWND hwnd, ATOM atom );

## 매개 변수

_hwnd_

검색된 유니코드에 의한 문자 조합을 지정합니다.

_atom_

> 지정된 플러그 인 파일 이름의 atom을 지정합니다.

## 반환 값

> 플러그 인이 해제된 경우, 반환 값은 TRUE입니다.
> 플러그 인이 해제되지 않은 경우, 반환 값은 FALSE입니다.