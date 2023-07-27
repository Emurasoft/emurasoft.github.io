# Editor\_RearrangeColumns

Rearranges CSV columns. You can use this inline function or explicitly send the [EE\_REARRANGE\_COLUMNS](../message/ee_rearrange_columns) message.

Editor\_RearrangeColumns( HWND hwnd, UINT nColumnArraySize, const INT\* piColumn );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nSize_

Specifies the number of columns specified in the _piColumn_ parameter.

_piColumn_

Specifies an array of integers, indicating the order of columns to be rearranged. For instance, "0, 2, 4" indicates the result will include the first, third, and fifth columns of the original CSV document.

## Return Values

If the message succeeds, the return value is zero. If the message fails,
the return value is nonzero.

## Version

Supported on Version 22.1 or later.
