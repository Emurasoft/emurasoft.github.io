# Editor\_InsertStringW

현재 커서 위치에 유니코드 문자열을 삽입합니다. 현재 속성에 따라 기존의 문자열을 덮어쓸수 있습니다. 이 인라인 함수를 사용하거나 [EE\_INSERT\_STRINGW](../message/ee_insert_stringw) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_InsertStringW( HWND hwnd, LPCWSTR szString, bool bKeepDestReturnType = false );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_szString_

> 삽입할 문자열을 지정합니다.

_bKeepDestReturnType_

> 대상 반환 유형 (CR 만, LF 만 또는 CR과 LF)이 유지되도록 지정합니다.
> 이 매개 변수가 생략된경우, EmEditor는 szString 매개 변수에서 지정된 반환 유형을 유지합니다.

## 반환 값

> 반환 값이 사용되지 않습니다.