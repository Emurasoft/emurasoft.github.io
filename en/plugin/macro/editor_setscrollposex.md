# Editor\_SetScrollPosEx

Specifies the scroll bar position. You can use this inline function or explicitly send the [EE\_SET\_SCROLL\_POS](../message/ee_set_scroll_pos) message.

Editor\_SetScrollPos( HWND hwnd, POINT\* pptPos, BOOL bCanMoveCursor );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pptPos_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the scroll bar positions. The
cursor position will not be changed.

_bCanMoveCursor_

If this parameter is TRUE and if the
[**Move** **Cursor by Scrolling** check box](../../dlg/properties/scroll/index) is selected, the cursor position will also move. If this parameter is FALSE, the cursor position will not move.

## Return Values

The return value is not used.

## Version

Supported on EmEditor Professional Version 5.00 or later.
