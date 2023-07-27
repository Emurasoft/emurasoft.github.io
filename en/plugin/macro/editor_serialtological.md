# Editor\_SerialToLogical

Converts the serial position to the logical coordinates. The serial position
is the zero-based index of the character from the beginning of the entire text.
You can use this inline function or explicitly send the
[EE\_SERIAL\_TO\_LOGICAL](../message/ee_serial_to_logical)
message.

Editor\_SerialToLogical( HWND hwnd, UINT nSerial, POINT\_PTR\* pptLogical );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nSerial_

Specifies a serial position to be converted.

_pptLogical_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the converted logical
coordinates.

## Return Values

The return value is not used.
