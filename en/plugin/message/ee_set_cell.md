# EE\_SET\_CELL

Sets the text on the specified cell. You can send this message explicitly or use the
[Editor\_SetCell](../macro/editor_setcell) inline function.

EE\_SET\_CELL

wParam = (WPARAM) (GET\_CELL\_INFO\*) pGetCellInfo;

lParam = (LPARAM) (LPWSTR) szString;

## Parameters

_pGetCellInfo_

> Pointer to the [GET\_CELL\_INFO](../structure/get_cell_info) structure.

_szString_

> Specifies a string to set.

## Return Values

> The return value is 0 or positive if succeeded, or negative if failed.