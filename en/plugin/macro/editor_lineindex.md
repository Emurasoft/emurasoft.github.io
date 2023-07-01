# Editor\_LineIndex

Retrieves the character index of the first character of a specified line in
EmEditor. A character index is the zero-based index of the character from the
beginning of the edit control. You can use this inline function or explicitly send
the [EE\_LINE\_INDEX](../message/ee_line_index)
message.

Editor\_LineIndex( HWND hwnd, BOOL bLogical, int yLine );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_bLogical_

> Specifies TRUE if the line number is by the logical coordinates. Specifies
> FALSE if the line number is by the display coordinates.

_yLine_

> Specifies the zero-based line number. A value of -1 specifies the current
> line number (the line that contains the cursor).

## Return Values

> The return value is the character index of the line specified in the _yLine_ parameter.
