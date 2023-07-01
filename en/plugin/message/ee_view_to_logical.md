# EE\_VIEW\_TO\_LOGICAL

Converts the display coordinates of a specified position to the logical
coordinates. You can send this message explicitly or use the
[Editor\_ViewToLogical](../macro/editor_viewtological)
inline function.

EE\_VIEW\_TO\_LOGICAL

wParam = (WPARAM) (POINT\_PTR\*) pptView;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical;

## Parameters

_pptView_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the display coordinates to be
> converted.

_pptLogical_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the converted logical
> coordinates.

## Return Values

> The return value is not used.
