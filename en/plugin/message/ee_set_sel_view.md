# EE\_SET\_SEL\_VIEW

Changes the starting and ending position of the selection. You can send
this message explicitly or use the
[Editor\_SetSelView](../macro/editor_setselview)
inline function.

```
EE_SET_SEL_VIEW
wParam = (WPARAM) (POINT_PTR*) pptSelStart;
lParam = (LPARAM) (POINT_PTR*) pptSelEnd;
```

## Parameters

_pptSelStart_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the starting position of the
selection. The position is by display coordinates.

_pptSelEnd_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the ending position of the
selection. The position is by display coordinates.

## Return Values

The return value is not used.
