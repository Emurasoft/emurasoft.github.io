# EE\_SET\_CARET\_POS

Moves the cursor position and optionally extends the selection. You can send this message explicitly or by
using the [Editor\_SetCaretPos](../macro/editor_setcaretpos) inline function or the [Editor\_SetCaretPosEx](../macro/editor_setcaretposex) inline function.

EE\_SET\_CARET\_POS

wParam = MAKEWPARAM( nLogical, bExtend );

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## Parameters

_nLogical_

Specifies a combination of the following values.

| Value | Meaning |
| --- | --- |
| POS\_VIEW | Display Coordinates |
| POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
| POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |
| POS\_CELL | CSV Cell Unit |
| POS\_SCROLL\_DONT\_CARE | The cursor position becomes where the scrolling becomes minimum. |
| POS\_SCROLL\_CENTER | The cursor position becomes near the center of the window. |
| POS\_SCROLL\_TOP | The cursor position becomes the top of the window. |

_bExtend_

Determines whether to extend the current selection. If _bExtend_ is
TRUE, then the active end of the selection moves to the location while the
anchor end remains where it is. Otherwise, both ends are moved to the
specified location.

_pptPos_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specified the cursor position.

## Return Values

The return value is not used.

## Version

Supported on Version 4.03 or later. However, POS\_SCROLL\_DONT\_CARE, POS\_SCROLL\_CENTER, and POS\_SCROLL\_TOP flags are supported on Version 6.00 or later.
