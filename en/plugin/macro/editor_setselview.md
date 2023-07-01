# Editor\_SetSelView

Changes the the starting and ending position of the selection. You can use this inline function or explicitly send the [EE\_SET\_SEL\_VIEW](../message/ee_set_sel_view) message.

Editor\_SetSelView( HWND hwnd, POINT\_PTR\* pptSelStart, POINT\_PTR\* pptSelEnd );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pptSelStart_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the starting position of the
> selection. The position is by display coordinates.

_pptSelEnd_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the ending position of the
> selection. The position is by display coordinates.

## Return Values

> The return value is not used.
