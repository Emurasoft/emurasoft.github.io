# EE\_SERIAL\_TO\_LOGICAL

Converts the serial position to the logical coordinates. The serial position
is the zero-based index of the character from the beginning of the entire text.
You can send this message explicitly or use the
[Editor\_SerialToLogical](../macro/editor_serialtological)
inline function.

EE\_SERIAL\_TO\_LOGICAL

wParam = (WPARAM) (UINT) nSerial;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical;

## Parameters

_nSerial_

Specifies a serial position to be converted.

_pptLogical_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the converted logical
coordinates.

## Return Values

The return value is not used.
