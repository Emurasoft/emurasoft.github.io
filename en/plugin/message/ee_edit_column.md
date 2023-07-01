# EE\_EDIT\_COLUMN

Moves, copies, deletes, or combines specified columns of the current CSV document. You can send this message explicitly or use the [Editor\_EditColumn](../macro/editor_editcolumn) inline function.

EE\_EDIT\_COLUMN

wParam = (WPARAM)(EDIT\_COLUMN\_INFO\*)pInfo;

lParam = 0;

## Parameters

_pInfo_

> Specifies the pointer to the [EDIT\_COLUMN\_INFO](../structure/edit_column_info) structure.

## Return Values

> The return value is S\_OK if succeeds.

## Version

> Supported on Version 19.7 or later.
