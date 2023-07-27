# EE\_GET\_CMD\_ID

플러그 인 command ID를 가져옵니다. 이 메시지를 명시적으로 또는
[Editor\_GetCmdID](../macro/editor_getcmdid) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_GET\_CMD\_ID

wParam = 0;

lParam = (LPARAM) (HINSTANCE) hInstance

## 매개 변수

_hInstance_

플러그 인 인스턴스 핸들을 지정합니다.

## 반환 값

이 플러그 인을 실행할 command ID를 반환합니다.
