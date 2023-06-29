# Editor\_GetOutlineLevel

Retrieves the outline level for the specified logical line. You can use this inline function or explicitly send the [EE\_GET\_OUTLINE\_LEVEL](../message/ee_get_outline_level) message.

Editor\_GetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nLogicalLine_

> Specifies a logical line.

## Return Values

> The return value is the outline level for the specified logical line. If an
> error occurs, the return value will be -1.

## Version

> Supported on EmEditor Professional Version 6.00 or later.