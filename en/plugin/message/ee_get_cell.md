# EE\_GET\_CELL

Retrieves the Unicode text on the specified cell. You can send this message
explicitly or use the
[Editor\_GetCell](../macro/editor_getcell) inline function.

EE\_GET\_CELL

wParam = (WPARAM) (GET\_CELL\_INFO\*) pGetCellInfo;

lParam = (LPARAM) (LPWSTR) szString;

## Parameters

_pGetCellInfo_

Pointer to the [GET\_CELL\_INFO](../structure/get_cell_info) structure.

_szString_

Pointer to the buffer that will receive the text.

## Return Values

If _pGetCellInfo->cch_ is zero, the return value is the required
size, in characters, for a buffer that can receive the text. If _pGetLineInfo->cch_ is not zero, the
return value is not used. If _pGetCellInfo->iColumn_ is -1, the return value is the number of columns.
