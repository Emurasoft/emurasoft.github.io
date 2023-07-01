# Editor\_GetColumn

Sets a column of text in CSV mode. You can use this inline function or explicitly send the
[EE\_GET\_COLUMN](../message/ee_get_column) message.

Editor\_GetColumn( HWND hwnd, COLUMN\_STRUCT\* pColumnStruct );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pColumnStruct_

> Pointer to the [COLUMN\_STRUCT](../structure/column_struct) structure.

## Return Values

> The return value is the size of the buffer including the terminating NULL in characters needed to retrieve the text if succeeded, or negative if failed. The return value can be larger than the exact size to retrieve the text.
