# EE\_SET\_CONFIGA

ASNI 문자열로 지정된 구성으로 변경합니다. 이 메시지를 명시적으로 보내거나
[Editor\_SetConfigA](../macro/editor_setconfiga) 인라인 함수를 사용할 수
있습니다.

EE\_SET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szConfigName;

## 매개 변수

_szConfigName_

ANSI 문자열로 구성을 지정합니다.

## 반환 값

반환 값이 사용되지 않습니다.
