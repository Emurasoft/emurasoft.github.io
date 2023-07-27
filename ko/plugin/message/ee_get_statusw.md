# EE\_GET\_STATUSW

상태 표시줄에 표시된 유니코드 텍스트를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetStatusW](../macro/editor_getstatusw) 인라인 함수를 사용할 수 있습니다.

EE\_GET\_STATUSW

wParam = nBufSize;

lParam = (LPARAM) (LPWSTR) szStatus;

## 매개 변수

_nBufSize_

종료된 null문자를 포함한 문자열을 검색하기위해 단어로 버퍼의 크기를 지정합니다.
_szMessage_ 가 null인 경우 0을 지정할 수 있습니다. 버퍼 크기가 충분하지 않은 경우,
_szMessage_ 는 문자열을 검색하지 않습니다.

_szStatus_

문자열을 검색하기 위해 버퍼를 지정합니다.NULL이 지정되는 경우, 문자열을 검색하기 위해 충분한 버퍼의 크기를 반환합니다.

## 반환 값

종료된 null 문자를 포함한 문자열을 검색하기에 충분한 버퍼의 크기를 단어로 반환합니다.
