# EE\_GET\_CONFIGA

ANSI 문자열로 선택된 구성의 이름을 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetConfigA](../macro/editor_getconfiga) 인라인 함수를 사용할 수 있습니다.

EE\_GET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPSTR) szConfigName;

## 매개 변수

_szConfigName_

> 구성 이름을 수신할 버퍼를 지정합니다. 버퍼의 크기는 최소 MAX\_CONFIG\_NAME 바이트이어야 합니다.

## 반환 값

> 반환 값이 사용되지 않습니다.
