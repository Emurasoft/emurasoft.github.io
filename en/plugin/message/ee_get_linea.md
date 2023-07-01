# EE\_GET\_LINEA

Retrieves the ANSI text on the specified line. You can send this message
explicitly or use the [Editor\_GetLineA](../macro/editor_getlinea) inline function.

EE\_GET\_LINEA

wParam = (WPARAM) (GET\_LINE\_INFO\*) pGetLineInfo;

lParam = (LPARAM) (LPSTR) szString;

## Parameters

_pGetLineInfo_

> Specifies the pointer to
> [GET\_LINE\_INFO](../structure/get_line_info)
> structure.

_szString_

> Pointer to the buffer that will receive the text.

## Return Values

> If _pGetLineInfo->cch_ is zero, the return value is the
> required size, in bytes, for a buffer that can receive the text. If _pGetLineInfo->cch_ is not zero, the return value is not used.
