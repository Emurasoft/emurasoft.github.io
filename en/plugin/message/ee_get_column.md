# EE\_GET\_COLUMN

Retrieves a column of text in CSV mode. You can send this message explicitly or use the
[Editor\_GetColumn](../macro/editor_getcolumn) inline function.

EE\_GET\_COLUMN

wParam = (WPARAM) 0;

lParam = (LPARAM) (COLUMN\_STRUCT\*) pColumnStruct;

## Parameters

_pColumnStruct_

> Pointer to the [COLUMN\_STRUCT](../structure/column_struct) structure.

## Return Values

> The return value is the size of the buffer including the terminating NULL in characters needed to retrieve the text if succeeded, or negative if failed. The return value can be larger than the exact size to retrieve the text.