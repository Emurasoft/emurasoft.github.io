# Editor\_GetLineA

Retrieves the ANSI text on the specified line. You can use this inline function or explicitly send the [EE\_GET\_LINEA](../message/ee_get_linea) message.

Editor\_GetLineA( HWND hwnd, GET\_LINE\_INFO\* pGetLineInfo, LPSTR szString );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pGetLineInfo_

> Pointer to the [GET\_LINE\_INFO](../structure/get_line_info) structure.

_szString_

> Pointer to the buffer that will receive the text.

## Return Values

> If _pGetLineInfo->cch_  is zero, the return value is the
> required size, in bytes, for a buffer that can receive the text. If _pGetLineInfo->cch_. is not zero, the return value is not used.
