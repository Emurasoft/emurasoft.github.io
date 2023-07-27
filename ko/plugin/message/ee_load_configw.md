# EE\_LOAD\_CONFIGW

유니코드 문자열로 지정된 이름의 구성을 다시로드합니다. 이 메시지를 명시적으로 보내거나
[Editor\_LoadConfigW](../macro/editor_loadconfigw) 인라인 함수를 사용할 수
있습니다.

EE\_LOAD\_CONFIGW

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szConfigName;

## 매개 변수

_szConfigName_

다시로드할 구성의 이름을 지정합니다.

## 반환 값

반환 값이 사용되지 않습니다.
