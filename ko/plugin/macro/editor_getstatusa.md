# Editor\_GetStatusA

상태 표시줄에 표시된 ANSI 텍스트를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_STATUSA](../message/ee_get_statusa) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetStatusA( HWND hwnd, LPSTR szStatus, UINT nBufSize );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nBufSize_

문자열을 검색하기 위해 종료된 null 문자를 포함한 문자 내 버퍼의 크기를 지정합니다.
_szStatus_ 가 NULL인 경우, 0을 지정할 수 있습니다. 버퍼의 크기가 충분하지 않은 경우, _szStatus_ 는
문자열을 검색하지 않습니다.

_szStatus_

문자열을 검색하기 위해 버퍼를 지정합니다.NULL이 지정되는 경우, 문자열을 검색하기 위해 충분한 버퍼의 크기를 반환합니다.

## 반환 값

종료된 null 문자를 포함한 문자열을 검색하기에 충분한 버퍼의 크기를 단어로 반환합니다.
