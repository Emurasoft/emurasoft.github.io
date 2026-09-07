# Editor\_GetTextW

Retrieves the document text. If the document contains more than `0x7ffffffe` UTF-16 code units, the text is truncated to that length. You can use this inline function or explicitly send the [EE\_GET\_TEXTW](../message/ee_get_textw) message.

Editor\_GetTextW( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nBufferSize_

The capacity of the buffer, in `WCHAR` elements, including space for the terminating null character.

_szBuffer_

A pointer to the buffer that receives the document text.

## Return Values

Returns the required buffer size, in `WCHAR` elements, including the terminating null character.

If the document contains more than `0x7ffffffe` UTF-16 code units, the return value is `0x7fffffff`. Returns zero if an error occurs.
