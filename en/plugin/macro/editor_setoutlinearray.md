# Editor\_SetOutlineArray

Sets the outline levels for the specified multiple lines. You can use this inline function or explicitly send the
[EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) message.

Editor\_SetOutlineArray( HWND hwnd, INT\_PTR nStartLine, INT\_PTR nCount, BYTE\* pLevelData );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nStartLine_

Specifies the first line of multiple lines.

_nCount_

Specifies the number of multiple lines.

_pLevelData_

Specifies an array of BYTE that specifies the outline levels.

## Return Values

The return value is FALSE if there was no change. Otherwise, the return
value is TRUE.

## Version

Supported in EmEditor Professional Version 13 or later.
