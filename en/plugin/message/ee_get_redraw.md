# EE\_GET\_REDRAW

Retrieves the flag that allows changes in EmEditor to be redrawn or prevents changes in EmEditor
to be redrawn. You can send this
message explicitly or use the [Editor\_GetRedraw inline function](../macro/editor_getredraw).

EE\_GET\_REDRAW

wParam = (WPARAM) 0;

lParam = (LPARAM) 0;

## Parameters

> None.

## Return Values

> Returns TRUE if the current flag allows changes in EmEditor to be redrawn or prevents changes in EmEditor to be redrawn. Otherwise, returns FALSE.

## Version

> Supported on Version 5.00 or later.
