# Editor\_SetOutlineLevel

Sets the outline level for the specified logical line. You can use this inline function or explicitly send the [EE\_SET\_OUTLINE\_LEVEL](../message/ee_set_outline_level) message.

Editor\_SetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine, int nLevel );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nLogicalLine_

Specifies a logical line.

_nLevel_

Specifies an outline level.

## Return Values

The return value is the old outline level for the specified logical line.
If an error occurs, the return value will be -1.

## Version

Supported on EmEditor Professional Version 6.00 or later.
