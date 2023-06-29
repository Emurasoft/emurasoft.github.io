# EE\_REDRAW

Allows changes in EmEditor to be redrawn or prevents changes in EmEditor to
be redrawn. You can send this message explicitly or use the
[Editor\_Redraw](../macro/editor_redraw) inline function.

EE\_REDRAW

wParam = (WPARAM)bRedraw;

lParam = (LPARAM)0;

## Parameters

_bRedraw_

> Specifies the redraw state. If this parameter is TRUE, the content can be
> redrawn after a change. If this parameter is FALSE, the content cannot be
> redrawn after a change.

## Return Values

> The return value is not used.