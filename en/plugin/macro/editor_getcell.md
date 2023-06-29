# Editor\_GetCell

Retrieves the Unicode text on the specified cell. You can use this inline function or explicitly send the
[EE\_GET\_CELL](../message/ee_get_cell) message.

Editor\_GetCell( HWND hwnd, GET\_CELL\_INFO\* pGetCellInfo, LPWSTR szString );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pGetCellInfo_

> Pointer to the [GET\_CELL\_INFO](../structure/get_cell_info) structure.

_szString_

> Pointer to the buffer that will receive the text.

## Return Values

> If _pGetCellInfo->cch_ is zero, the return value is the required
> size, in characters, for a buffer that can receive the text. If _pGetLineInfo->cch_ is not zero, the
> return value is not used. If _pGetCellInfo->iColumn_ is -1, the return value is the number of columns.