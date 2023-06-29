# Editor\_SetCell

Sets the text on the specified cell. You can use this inline function or explicitly send the
[EE\_SET\_CELL](../message/ee_set_cell) message.

Editor\_SetCell( HWND hwnd, GET\_CELL\_INFO\* pGetCellInfo, LPCWSTR szString );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pGetCellInfo_

> Pointer to the [GET\_CELL\_INFO](../structure/get_cell_info) structure.

_szString_

> Specifies a string to set.

## Return Values

> The return value is 0 or positive if succeeded, or negative if failed.