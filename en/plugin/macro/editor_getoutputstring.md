# Editor\_GetOutputString

Retrieves the text in the output bar. You can use this inline function or explicitly send the [EE\_GET\_OUTPUT\_STRING](../message/ee_get_output_string)
message.

Editor\_GetOutputString( HWND hwnd, UINT cchBuf, LPWSTR pBuf );

## Parameters

_cchBuf_

> Specifies the size of the buffer in characters including the terminating NULL character.

_pBuf_

> Specifies the pointer to the buffer that receives the text.

## Return Values

> The return value is the size of the buffer in characters including the terminating NULL character needed to receive the text.

## Version

> Supported on EmEditor Version 9.00 or later.
