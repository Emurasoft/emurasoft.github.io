# Editor\_GetConfigA

ANSI 문자열로 선택된 구성 이름을 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_CONFIGA](../message/ee_get_configa) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetConfigA( HWND hwnd, LPSTR szConfigName );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_szConfigName_

구성 이름을 수신할 버퍼를 지정합니다. 버퍼의 크기는 최소 MAX\_CONFIG\_NAME 바이트이어야 합니다.

## 반환 값

반환 값이 사용되지 않습니다.
