# EE\_ENUM\_HIGHLIGHT

Enumerates highlighted strings. You can send this message
explicitly or use the [Editor\_EnumHighlight](../macro/editor_enumhighlight) inline function.

```
EE_ENUM_HIGHLIGHT
wParam = (WPARAM) (size_t) cchBuf;
lParam = (LPARAM) (LPWSTR) pBuf;
```

## Parameters

_cchBuf_

Specifies the size of the buffer in characters. Note that two null characters will be added at the end of the list of highlighted strings. If 0 is specified, this message returns the size necessary to retrieve the list of highlighted strings.

_pBuf_

Specifies the pointer to the buffer to retrieve the list of highlighted strings. In this buffer, the list of highlighted strings each separated by a null character will be retrieved. Two null characters will be added at the end of the list of
highlighted strings. If 0 is specified, pBuf can be NULL.

The first character of each string represents the color and a combination of the following values.

|     |     |
| --- | --- |
| From 0 to 9 | color. Use HIGHLIGHT\_COLOR\_MASK for mask. |
| HIGHLIGHT\_WORD | whole world only. |
| HIGHLIGHT\_RIGHT\_SIDE | highlight right side. |
| HIGHLIGHT\_INSIDE\_TAG | inside tag only. |
| HIGHLIGHT\_REG\_EXP | regular expression. |
| HIGHLIGHT\_CASE | match case. |
| HIGHLIGHT\_RIGHT\_ALL | highlight right all. |

## Return Values

The return value is the size necessary to retrieve the list of highlighted strings.

## Version

Supported on Version 7.00 or later.
