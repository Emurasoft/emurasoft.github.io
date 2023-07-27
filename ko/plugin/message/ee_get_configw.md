# EE\_GET\_CONFIGW

유니코드 문자열로 선택된 구성의 이름을 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_DocGetConfigW](../macro/editor_docgetconfigw) 인라인 함수 또는
[Editor\_GetConfigW](../macro/editor_getconfigw) 인라인 함수를 사용 할 수 있습니다.

EE\_GET\_CONFIGW

wParam = MAKEWPARAM(0, (iDoc)+1);

lParam = (LPARAM) (LPWSTR) szConfigName;

## 매개 변수

_iDoc_

대상 문서의 인덱스를 지정합니다.
1로 시작하는 인덱스는 wParam의 상위 단어에 지정되어야 합니다.
wParam의 상위 단어에 0이 지정되면, 현재 활성화 중인 문서가 대상으로 지정됩니다.

_szConfigName_

구성 이름을 수신 할 버퍼를 지정합니다. 버퍼의 크기는 최소 단어로 MAX\_CONFIG\_NAME가 되어야 합니다.

## 반환 값

반환 값이 사용되지 않습니다.
