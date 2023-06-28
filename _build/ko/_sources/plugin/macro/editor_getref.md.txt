# Editor\_GetRef

지정된 플러그 인의 참조 번호를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_REF](../message/ee_get_ref)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetRef( HWND hwnd, ATOM atom );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_atom_

> 지정된 플러그 인 파일 이름의 atom을 지정합니다.

## 반환 값

> 반환 값은 지정된 플러그 인의 참조 번호입니다. 반환 값이 0인 경우, 지정된 플러그인은 EmEditor로부터
> 안전하게 언로드될 수 있습니다.