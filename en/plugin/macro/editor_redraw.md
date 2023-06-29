# Editor\_Redraw

Allows changes in EmEditor to be redrawn or prevents changes in EmEditor from
being redrawn. You can use this inline function or explicitly send the
[EE\_REDRAW](../message/ee_redraw) message.

Editor\_Redraw( HWND hwnd, BOOL bRedraw );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_bRedraw_

> Specifies the redraw state. If this parameter is TRUE, the content can be
> redrawn after a change. If this parameter is FALSE, the content cannot be
> redrawn after a change.

## Return Values

> The return value is not used.