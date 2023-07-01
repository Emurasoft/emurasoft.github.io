# EE\_GET\_SEL\_TEXTW

Retrieves the selected Unicode text. You can send this message explicitly or
by using the [Editor\_GetSelTextW](../macro/editor_getseltextw) inline function.

EE\_GET\_SEL\_TEXTW

wParam = (WPARAM) (UINT) nBufferSize;

lParam = (LPARAM) (LPWSTR) szBuffer;

## Parameters

_nBufferSize_

> Specifies the maximum number of characters in words to copy to the buffer,
> including the NULL character.

_szBuffer_

> Pointer to the buffer that will receive the text.

## Return Values

> If _nBufferSize_. is zero, the return value is the required size, in words,
> for a buffer that can receive the text. If _nBufferSize_ is not zero, the return value is not used.
