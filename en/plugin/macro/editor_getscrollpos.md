# Editor\_GetScrollPos

Retrieves the current positions of the scroll bars. You can use this inline function or explicitly send the
[EE\_GET\_SCROLL\_POS](../message/ee_get_scroll_pos)
message.

Editor\_GetScrollPos( HWND hwnd, POINT\_PTR\* pptPos );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pptPos_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the scroll bar positions.

## Return Values

> The return value is not used.