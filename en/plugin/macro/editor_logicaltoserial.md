# Editor\_LogicalToSerial

Converts the logical coordinates to the serial position. The serial position
is the zero-based index of the character from the beginning of the entire text.
You can use this inline function or explicitly send the
[EE\_LOGICAL\_TO\_SERIAL](../message/ee_logical_to_serial)
message.

Editor\_LogicalToSerial( HWND hwnd, POINT\_PTR\* pptLogical );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pptLogical_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the logical coordinates to be
> converted.

## Return Values

> Return the serial position.
