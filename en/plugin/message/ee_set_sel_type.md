# EE\_SET\_SEL\_TYPE

Sets the type of selection status. You can send this message explicitly or
use the [Editor\_SetSelType](../macro/editor_setseltype) inline function or [Editor\_SetSelTypeEx](../macro/editor_setseltypeex) inline function.

EE\_SET\_SEL\_TYPE

wParam = (WPARAM) (BOOL) bNeedAlways;

lParam = (LPARAM) nSelType;

## Parameters

_bNeedAlways_

If this parameter is TRUE, the type of selection status can be set even if none is selected. If this parameter is FALSE, SEL\_TYPE\_NONE will cancel the selection.

_nSelType_

You can specify a combination of the following values. However, SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, SEL\_TYPE\_BOX cannot be
combined. Only SEL\_TYPE\_KEYBOARD can be combined with SEL\_TYPE\_NONE,
SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, or SEL\_TYPE\_BOX.

|     |     |
| --- | --- |
| SEL\_TYPE\_NONE | Not selected. |
| SEL\_TYPE\_CHAR | Stream selection mode. |
| SEL\_TYPE\_LINE | Line selection mode. |
| SEL\_TYPE\_BOX | Vertical selection mode. |
| SEL\_TYPE\_KEYBOARD | Specifies the keyboard selection mode. This value can be combined with <br> another value. |

## Return Values

Not used.

## Version

Supported on EmEditor Professional Version 3.00 or later. However, bNeedAlways is supported on Version 5.00 or later. On the previous versions, bNeedAlways is assumed to be FALSE.
