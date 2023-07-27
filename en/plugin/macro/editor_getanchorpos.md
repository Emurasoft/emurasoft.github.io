# Editor\_GetAnchorPos

Retrieves the origin point of the selection. You can use this inline function
or explicitly send the [EE\_GET\_ANCHOR\_POS](../message/ee_get_anchor_pos) message.

Editor\_GetAnchorPos( HWND hwnd, int nLogical, POINT\_PTR\* pptPos );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nLogical_

Specifies one of the following values.

| Value | Meaning |
| --- | --- |
| POS\_VIEW | Display Coordinates |
| POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
| POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |

_pptPos_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the origin point of the
selection.

## Return Values

The return value is not used.
