# EE\_DEV\_TO\_VIEW

Converts the device (client) coordinates of a specified position to the
display coordinates. You can send this message explicitly or use the
[Editor\_DevToView](../macro/editor_devtoview) inline function.

EE\_DEV\_TO\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptDev;

lParam = (LPARAM) (POINT\_PTR\*) pptView;

## Parameters

_pptDev_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the device coordinates to be
> converted.

_pptView_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) to receive the converted display coordinates.

## Return Values

> The return value is not used.