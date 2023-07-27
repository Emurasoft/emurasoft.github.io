# EE\_GET\_MARGIN

Retrieves the margin size. You can send this message explicitly or by using
the [Editor\_GetMargin](../macro/editor_getmargin)
inline function.

EE\_GET\_MARGIN

wParam = 0;

lParam = 0;

## Parameters

None.

## Return Values

Returns the currently selected margin size. If the normal line margin size
and the quoted line margin size are different, the larger margin will be
returned. If lines are wrapped by the window size, the return value will
depend on the current window size.
