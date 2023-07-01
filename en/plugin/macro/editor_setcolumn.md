# Editor\_SetColumn

Sets a column of text. You can use this inline function or explicitly send the
[EE\_SET\_COLUMN](../message/ee_set_column) message.

Editor\_SetColumn( HWND hwnd, COLUMN\_STRUCT\* pColumnStruct );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pSetLineInfo_

> Pointer to the [COLUMN\_STRUCT](../structure/column_struct) structure.

## Return Values

> The return value is 0 or positive if succeeded, or negative if failed.
