# Editor\_GetWord

Retrieves a word at the cursor position. You can use this inline function or explicitly send the [EE\_GET\_WORD](../message/ee_get_word) message.

Editor\_GetWord( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nBufferSize_

Specifies the maximum number of characters in characters to copy to the buffer,
including the NULL character.

_szBuffer_

Pointer to the buffer that will receive the text.

## Return Values

If _nBufferSize_ is zero, the return value is the required size, in characters,
for a buffer that can receive the text. If _nBufferSize_ is not zero, the
return value is not used.

## Version

Supported on EmEditor Version 10.00 or later.
