# EE\_GET\_SEL\_TEXTA

Retrieves the selected ANSI text. You can send this message explicitly or by
using the [Editor\_GetSelTextA](../macro/editor_getseltexta) inline function.

EE\_GET\_SEL\_TEXTA

wParam = (WPARAM) (UINT) nBufferSize;

lParam = (LPARAM) (LPSTR) szBuffer;

## Parameters

_nBufferSize_

Specifies the maximum number of characters in bytes to copy to the buffer,
including the NULL character.

_szBuffer_

Pointer to the buffer that will receive the text.

## Return Values

If _nBufferSize_. is zero, the return value is the required size, in
bytes, for a buffer that can receive the text. If _nBufferSize_. is not
zero, the return value is not used.
