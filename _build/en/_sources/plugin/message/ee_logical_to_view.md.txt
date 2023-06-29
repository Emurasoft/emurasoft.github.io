# EE\_LOGICAL\_TO\_VIEW

Converts the logical coordinates to the display coordinates. You can send this
message explicitly or use the
[Editor\_LogicalToView](../macro/editor_logicaltoview)
inline function.

EE\_LOGICAL\_TO\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptView;

## Parameters

_pptLogical_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the logical coordinates to be
> converted.

_pptView_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) to receive the converted display coordinates.

## Return Values

> The return value is not used.