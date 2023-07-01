# EE\_GET\_STATUSW

Retrieves the Unicode text displayed on the status bar. You can send this
message explicitly or use the [Editor\_GetStatusW](../macro/editor_getstatusw) inline function.

EE\_GET\_STATUSW

wParam = nBufSize;

lParam = (LPARAM) (LPWSTR) szStatus;

## Parameters

_nBufSize_

> Specifies the size of buffer in characters to retrieve the string including
> the terminating null character. You can specify 0 if _szStatus_ is
> NULL. If the buffer size is not enough, _szStatus_ will retrieve no
> string.

_szStatus_

> Specifies the buffer to retrieve the string. If NULL is specified, returns
> the size of the buffer enough to retrieve the string.

## Return Values

> Returns the size of the buffer in characters enough to retrieve the string
> including the terminating null character.
