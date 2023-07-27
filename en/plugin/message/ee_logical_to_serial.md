# EE\_LOGICAL\_TO\_SERIAL

Converts the logical coordinates to the serial position. The serial position
is the zero-based index of the character from the beginning of the entire text.
You can send this message explicitly or use the
[Editor\_LogicalToSerial](../macro/editor_logicaltoserial)
inline function.

EE\_LOGICAL\_TO\_SERIAL

wParam = 0;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical

## Parameters

_pptLogical_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the logical coordinates to be
converted.

## Return Values

Return the serial position.
