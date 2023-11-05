# EE\_SET\_COLUMN

Sets a column of text in CSV mode. You can send this message explicitly or use the
[Editor\_SetColumn](../macro/editor_setcolumn) inline function.

```
EE_SET_COLUMN
wParam = (WPARAM) 0;
lParam = (LPARAM) (COLUMN_STRUCT*) pColumnStruct;
```

## Parameters

_pColumnStruct_

Pointer to the [COLUMN\_STRUCT](../structure/column_struct) structure.

## Return Values

The return value is 0 or positive if succeeded, or negative if failed.
