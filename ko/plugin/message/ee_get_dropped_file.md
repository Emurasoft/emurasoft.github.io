# EE\_GET\_DROPPED\_FILE

가장 최근에 삭제한 파일을 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetDroppedFile](../macro/editor_getdroppedfile) 인라인 함수를 사용할 수 있습니다.

EE\_GET\_CONFIGW

wParam = (WPARAM) (int) nIndex;

lParam = (LPARAM) (LPWSTR) pszBuf;

## 매개 변수

_nIndex_

삭제된 파일의 인덱스를 지정합니다. 0으로 시작하는 인덱스가 지정되어야 합니다.
-1이 지정되면, 삭제된 파일의 전체 숫자가 반환됩니다.

_pszBuf_

삭제된 파일 이름을 수신 할 버퍼를 지정합니다.
버퍼의 크기는 적어도 문자로 MAX\_PATH가 되어야 합니다.
-1이 nIndex에 지정되는 경우 이 매개 변수는 NULL이 될 수 있습니다.

## 반환 값

지정된 인덱스에 대한 삭제된 파일이 존재하는 경우 반환 값은 0이 아닙니다.
nIndex에 -1이 지정되면, 반환 값은 삭제된 파일의 전체 숫자가 됩니다.

## 버전

EmEditor 버전 8 이상에서만 지원됩니다.
