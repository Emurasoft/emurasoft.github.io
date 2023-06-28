# Editor\_AddRef

플러그 인의 참조 번호를 증가합니다. 이 인라인 함수를 사용하거나 [EE\_ADD\_REF](../message/ee_add_ref) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_AddRef( HWND hwnd, HINSTANCE hInstance );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_hInstance_

> 플러그 인을 위한 인스턴스 핸들을 지정합니다.

## 반환 값

> 반환 값은 증가한 후의 플러그 인 참조 번호입니다. 반환 값이 0과 같거나 그보다 작은 경우, 지정된 플러그 인은 EmEditor에서 안전하게 언로드 될 수 있습니다.