# Editor\_DocGetLines

Retrieves the number of the lines for the specified document. You can use this inline function or explicitly send the [EE\_GET\_LINES](../message/ee_get_lines) message.

Editor\_GetLines( HWND hwnd, int iDoc, int nLogical );

Editor\_GetLines( HWND hwnd, HEEDOC hDoc, int nLogical );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iDoc_

> Specifies the index of the target document. If -1 is specified, the currently active document will be targeted.

_hDoc_

> Specifies the handle to the target document. If NULL is specified, the currently active document will be targeted.

_nLogical_

> Specifies one of the following Values.
>
> | Value | Meaning |
> | --- | --- |
> | POS\_VIEW | Display Coordinates |
> | POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
> | POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |

## Return Values

> Returns the number of the lines in EmEditor. If the last line is ends with
> a return, the line will be counted. If the text is empty, returns one.