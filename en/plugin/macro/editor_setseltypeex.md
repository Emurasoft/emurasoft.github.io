# Editor\_SetSelTypeEx

Sets the type of selection status. You can use this inline function or explicitly send
the [EE\_SET\_SEL\_TYPE message](../message/ee_set_sel_type).

Editor\_SetSelTypeEx( hwnd, bNeedAlways, nSelType );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_bNeedAlways_

> If this parameter is TRUE, the type of selection status can be set even if none is selected. If this parameter is FALSE, SEL\_TYPE\_NONE will cancel the selection.

_nSelType_

> You can specify a combination of the following values. However,
> SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, SEL\_TYPE\_BOX cannot be
> combined. Only SEL\_TYPE\_KEYBOARD can be combined with SEL\_TYPE\_NONE,
> SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, or SEL\_TYPE\_BOX.
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_NONE | Not selected. |
> | SEL\_TYPE\_CHAR | Stream selection mode. |
> | SEL\_TYPE\_LINE | Line selection mode. |
> | SEL\_TYPE\_BOX | Vertical selection mode. |
> | SEL\_TYPE\_KEYBOARD | Specifies the keyboard selection mode. This value can be combined with <br> another value. |

## Return Values

> Not used.

## Version

> Supported on EmEditor Professional Version 5.00 or later.
