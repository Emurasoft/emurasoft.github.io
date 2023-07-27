# Editor\_GetSelTextW

Retrieves the selected Unicode text. You can use this inline function or explicitly send the [EE\_GET\_SEL\_TEXTW](../message/ee_get_sel_textw) message.

Editor\_GetSelTextW( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nBufferSize_

Specifies the maximum number of characters in words to copy to the buffer,
including the NULL character.

_szBuffer_

Pointer to the buffer that will receive the text.

## Return Values

If _nBufferSize_ is zero, the return value is the required size, in words,
for a buffer that can receive the text. If _nBufferSize_ is not zero, the
return value is not used.
