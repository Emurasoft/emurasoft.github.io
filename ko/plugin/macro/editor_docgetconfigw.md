# Editor\_DocGetConfigW

유니코드 문자열로 지정된 문서를 위해 선택된 구성 이름을 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_CONFIGW](../message/ee_get_configw) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_DocGetConfigW( HWND hwnd, int iDoc, LPWSTR szConfigName );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_iDoc_

> 대상 문서의 인덱스를 지정합니다. -1이 지정된 경우, 현재 활성화 중인 문서가 대상으로 지정됩니다.

_szConfigName_

> 구성 이름을 수신할 버퍼를 지정합니다. 버퍼의 크기는 최소 MAX\_CONFIG\_NAME 바이트이어야 합니다.

## 반환 값

> 반환 값이 사용되지 않습니다.

## 버전

> 엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.
