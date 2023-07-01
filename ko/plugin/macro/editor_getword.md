# Editor\_GetWord

단어를 커서 위치에 반환합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_WORD](../message/ee_get_word) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetWord( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nBufferSize_

> NULL문자를 포함하여 버퍼에 복사할 단어의 최대 수를 단어로 지정합니다.

_szBuffer_

> 텍스트를 수실 할 버퍼에 대한 포인터 입니다.

## 반환 값

> _nBufferSize_ 가 0인 경우, 텍스트를 수신할 수 있는 버퍼의 필요한 크기가 단어로 반환됩니다.
> _nBufferSize_ 가 0이 아닌 경우, 반환 값이 사용되지 않습니다.

## 버전

> EmEditor 버전 10.00 이상에서만 지원됩니다.
