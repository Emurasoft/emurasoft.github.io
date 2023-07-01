# Editor\_GetSelTextA

Retrieves the selected ANSI text. You can use this inline function or explicitly send the [EE\_GET\_SEL\_TEXTA](../message/ee_get_sel_texta) message.

Editor\_GetSelTextA( HWND hwnd, UINT nBufferSize, LPSTR szBuffer );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nBufferSize_

> Specifies the maximum number of characters in bytes to copy to the buffer,
> including the NULL character.

_szBuffer_

> Pointer to the buffer that will receive the text.

## Return Values

> If _nBufferSize_. is zero, the return value is the required size, in
> bytes, for a buffer that can receive the text. If _nBufferSize_ is not
> zero, the return value is not used.
