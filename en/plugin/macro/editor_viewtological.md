# Editor\_ViewToLogical

Convert the display coordinates of a specified position to the logical
coordinates. You can use this inline function or explicitly send the
[EE\_VIEW\_TO\_LOGICAL](../message/ee_view_to_logical)
message.

Editor\_ViewToLogical( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptLogical );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pptView_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the display coordinates to be
> converted.

_pptLogical_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the converted logical
> coordinates.

## Return Values

> The return value is not used.