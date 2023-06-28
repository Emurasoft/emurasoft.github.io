# Editor\_LoadConfigA

ANSI 문자열로 지정된 이름의 구성을 다시로드합니다. 이 인라인 함수를 사용하거나 [EE\_LOAD\_CONFIGA](../message/ee_load_configa) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_LoadConfigA( HWND hwnd, LPCSTR szConfigName );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_szConfigName_

> 다시로드할 구성의 이름을 지정합니다.

## 반환 값

> 반환 값이 사용되지 않습니다.