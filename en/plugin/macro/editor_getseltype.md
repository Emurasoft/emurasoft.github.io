# Editor\_GetSelType

Obtains the type of selection status. You can use this inline function or explicitly send the [EE\_GET\_SEL\_TYPE](../message/ee_get_sel_type) message.

Editor\_GetSelType( HWND hwnd );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

## Return Values

> Returns a combination of the following values. SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, and SEL\_TYPE\_BOX cannot be combined. Only SEL\_TYPE\_KEYBOARD can be combined with other values.

> | Value | Meaning |
> | --- | --- |
> | SEL\_TYPE\_NONE | None is selected. |
> | SEL\_TYPE\_CHAR | Characters are selected. |
> | SEL\_TYPE\_LINE | Lines are selected. |
> | SEL\_TYPE\_BOX | Boxes are selected. |
> | SEL\_TYPE\_KEYBOARD | Selected by the keyboard. |

## Version

> Supported on EmEditor Professional Version 3.00 or later.
