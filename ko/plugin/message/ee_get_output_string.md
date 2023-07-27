# EE\_GET\_OUTPUT\_STRING

출력 모음에 텍스트를 검색합니다. 이 메시지를 명시적으로 또는
[Editor\_GetOutputString](../macro/editor_getoutputstring) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_GET\_OUTPUT\_STRING

wParam = (WPARAM) (UINT) cchBuf;

lParam = (LPARAM) (LPWSTR) pBuf;

## 매개 변수

_cchBuf_

종료된 NULL 문자를 포함한 문자에 버퍼 크기를 지정합니다.

_pBuf_

텍스트를 수신하는 버퍼에 대한 포인터를 지정합니다.

## 반환 값

반환 값은 텍스트를 수신하는데 필요한 종료된 NULL 문자를 포함한 문자에 버퍼 크기에 해당합니다.

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
