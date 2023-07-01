# Editor\_LineFromChar

Retrieves the index of the line that contains the specified character index
(the serial position). A character index is the zero-based index of the
character from the beginning of the entire text. You can use this inline function or explicitly send the
[EE\_LINE\_FROM\_CHAR](../message/ee_line_from_char)
message.

Editor\_LineFromChar( HWND hwnd, int nLogical, UINT nSerialIndex );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nLogical_

> Specify one of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | POS\_VIEW | Display Coordinates |
> | POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
> | POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |

_nSerialIndex_

> Specifies the character index of the character contained in the line whose
> number is to be retrieved. If this parameter is -1, EE\_LINE\_FROM\_CHAR
> retrieves the line number of the current line (the line containing the
> cursor).

## Return Values

> The return value is the zero-based line number of the line containing the
> character index specified by _nSerialIndex_.
