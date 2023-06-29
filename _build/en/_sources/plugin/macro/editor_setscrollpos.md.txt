# Editor\_SetScrollPos

Specifies the scroll bar position. You can use this inline function or explicitly send the [EE\_SET\_SCROLL\_POS](../message/ee_set_scroll_pos) message.

Editor\_SetScrollPos( HWND hwnd, POINT\_PTR\* pptPos );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pptPos_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the scroll bar positions. The
> cursor position will not be changed.

## Return Values

> The return value is not used.