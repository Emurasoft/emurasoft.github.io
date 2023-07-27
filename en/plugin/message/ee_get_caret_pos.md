# EE\_GET\_CARET\_POS

Retrieves the current cursor position. You can send this message explicitly
or by using the [Editor\_GetCaretPos](../macro/editor_getcaretpos) inline function.

EE\_GET\_CARET\_POS

wParam = (WPARAM) (int) nLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## Parameters

_nLogical_

Specifies one of the following values.

| Value | Meaning |
| --- | --- |
| POS\_VIEW | Display Coordinates |
| POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
| POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |
| POS\_CELL | CSV Cell Unit |

_pptPos_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the current cursor position.

## Return Values

The return value is not used.
