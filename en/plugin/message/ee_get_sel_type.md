# EE\_GET\_SEL\_TYPE

Obtains the type of selection status. You can send this message explicitly or
by using the [Editor\_GetSelType](../macro/editor_getseltype) inline function or [Editor\_GetSelTypeEx](../macro/editor_getseltypeex) inline function.

```
EE_GET_SEL_TYPE
wParam = (WPARAM) (BOOL) bNeedAlways;
lParam = (LPARAM)0;
```

## Parameters

_bNeedAlways_

If this parameter is TRUE, EE\_GET\_SEL\_TYPE returns the type of selection status even if none is selected. If this parameter is FALSE, EE\_GET\_SEL\_TYPE returns SEL\_TYPE\_NONE if none is selected.

## Return Values

Returns a combination of the following values. SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, and SEL\_TYPE\_BOX cannot be combined. SEL\_TYPE\_KEYBOARD and SEL\_TYPE\_SELECTED can be combined with other
values. If bNeedAlways is TRUE and if text is selected, a logical sum with SEL\_TYPE\_SELECTED will be returned. If bNeedAlways is FALSE, SEL\_TYPE\_SELECTED will not be used.

| Value | Meaning |
| --- | --- |
| SEL\_TYPE\_NONE | None is selected. |
| SEL\_TYPE\_CHAR | Characters are selected. |
| SEL\_TYPE\_LINE | Lines are selected. |
| SEL\_TYPE\_BOX | Boxes are selected. |
| SEL\_TYPE\_KEYBOARD | Selected by the keyboard. |
| SEL\_TYPE\_SELECTED | Selected (when bNeedAlways = TRUE). |

## Version

Supported on EmEditor Professional Version 3.00 or later. However, bNeedAlways is supported on Version 5.00 or later. On the previous versions, bNeedAlways is assumed to be FALSE.
