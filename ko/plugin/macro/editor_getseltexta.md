# Editor\_GetSelTextA

선택된 ANSI 텍스트를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_SEL\_TEXTA](../message/ee_get_sel_texta) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetSelTextA( HWND hwnd, UINT nBufferSize, LPSTR szBuffer );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nBufferSize_

NULL문자를 포함하여 버퍼에 복사하려는 문자의 최대 수는 바이트로 지정합니다.

_szBuffer_

텍스트를 수실 할 버퍼에 대한 포인터 입니다.

## 반환 값

_nBufferSize_. 가 0인 경우, 반환 값은 텍스트를 수신 할 수 있는 버퍼를 위해 필요한 크기 (바이트) 입니다.
_nBufferSize_.가 0이 아닌 경우, 반환 값이 사용되지 않습니다.
