# EE\_GET\_ANCHOR\_POS

Retrieves the origin point of the selection. You can send this message explicitly
or by using the [Editor\_GetAnchorPos](../macro/editor_getanchorpos) inline function.

EE\_GET\_ANCHOR\_POS

wParam = (WPARAM) (int) nLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## Parameters

_nLogical_

> Specifies one of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | POS\_VIEW | Display Coordinates |
> | POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
> | POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |
> | POS\_CELL | CSV Cell Unit |

_pptPos_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the origin point of the
> selection.

## Return Values

> The return value is not used.