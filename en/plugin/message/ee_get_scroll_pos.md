# EE\_GET\_SCROLL\_POS

Retrieves the current positions of the scroll bars. You can send this message
explicitly or use the
[Editor\_GetScrollPos](../macro/editor_getscrollpos)
inline function.

EE\_GET\_SCROLL\_POS

wParam = 0;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## Parameters

_pptPos_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the scroll bar positions.

## Return Values

The return value is not used.
