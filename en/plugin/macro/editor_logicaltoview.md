# Editor\_LogicalToView

Converts the logical coordinates to the display coordinates. You can use this inline function or explicitly send the [EE\_LOGICAL\_TO\_VIEW](../message/ee_logical_to_view) message.

Editor\_LogicalToView( HWND hwnd, POINT\_PTR\* pptLogical, POINT\_PTR\* pptView );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pptLogical_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the logical coordinates to be
> converted.

_pptView_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) to receive the converted display coordinates.

## Return Values

> The return value is not used.
