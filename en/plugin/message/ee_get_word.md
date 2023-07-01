# EE\_GET\_WORD

Retrieves a word at the cursor position. You can send this message explicitly or
by using the [Editor\_GetWord](../macro/editor_getword) inline function.

EE\_GET\_WORD

wParam = (WPARAM) (UINT) nBufferSize;

lParam = (LPARAM) (LPWSTR) szBuffer;

## Parameters

_nBufferSize_

> Specifies the maximum number of characters in characters to copy to the buffer,
> including the NULL character.

_szBuffer_

> Pointer to the buffer that will receive the text.

## Return Values

> If _nBufferSize_. is zero, the return value is the required size, in characters,
> for a buffer that can receive the text. If _nBufferSize_ is not zero, the return value is not used.

## Version

> Supported on EmEditor Version 10.00 or later.
