# EE\_INSERT\_STRINGA

Inserts an ANSI string into the current cursor position. You can send this
message explicitly or use the
[Editor\_InsertStringA \
macro](../macro/editor_insertstringa), [Editor\_InsertA macro](../macro/editor_inserta), or
[Editor\_OverwriteA](../macro/editor_overwritea) inline function.

EE\_INSERT\_STRINGA

wParam = nInsertType;

lParam = (LPARAM) (LPCSTR) szString;

## Parameters

_nInsertType_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | OVERWRITE\_PER\_PROP | Inserts or Overwrites depending on the current Insert/Overwrite status. |
> | OVERWRITE\_INSERT | Always inserts, and does not overwrite the existing string. |
> | OVERWRITE\_OVERWRITE | Always overwrites the existing string. |
> | KEEP\_SOURCE\_RETURN\_TYPE | Keep the return type (CR only, LF only or both CR and LF) specified in the szString parameter. |
> | KEEP\_DEST\_RETURN\_TYPE | Keep the destination return type (CR only, LF only or both CR and LF). |

_szString_

> Specifies the string to be inserted.

## Return Values

> The return value is not used.

## Version

> KEEP\_SOURCE\_RETURN\_TYPE and KEEP\_DEST\_RETURN\_TYPE flags are supported on EmEditor Version 7.00 or later.