# Editor\_GetCmdID

플러그 인 command ID를 가져옵니다. 이 인라인 함수를 사용하거나 [EE\_GET\_CMD\_ID](../message/ee_get_cmd_id)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetCmdID( HWND hwnd, HINSTANCE hInstance );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_hInstance_

플러그 인 인스턴스 핸들을 지정합니다.

## 반환 값

이 플러그 인을 실행할 command ID를 반환합니다.
