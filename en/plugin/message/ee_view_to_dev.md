# EE\_VIEW\_TO\_DEV

Converts the display coordinates of a specified position to the device
(client) coordinates. You can send this message explicitly or use the
[Editor\_ViewToDev](../macro/editor_viewtodev) inline function.

EE\_VIEW\_TO\_DEV

wParam = (WPARAM) (POINT\_PTR\*) pptView;

lParam = (LPARAM) (POINT\_PTR\*) pptDev;

## Parameters

_pptView_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the display coordinates to be
> converted.

_pptDev_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) to receive the converted device coordinates. The x or y value of this structure might become LONG\_PTR\_MIN or LONG\_PTR\_MAX
> the specified position is invalid or the specified position is far from the screen rectangle.

## Return Values

> The return value is not used.
