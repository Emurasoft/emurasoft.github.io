# EE\_GET\_STATUSA

Retrieves the ANSI text displayed on the status bar. You can send this
message explicitly or use the [Editor\_GetStatusA inline function](../macro/editor_getstatusa).

EE\_GET\_STATUSA

wParam = nBufLen;

lParam = (LPARAM) (LPSTR) szMessage;

## Parameters

_nBufLen_

Specifies the size of buffer in characters to retrieve the string including the terminating null character. You can specify 0 if _szMessage_ is NULL. If the buffer size is not enough, _szMessage_ will retrieve no string.

_szMessage_

Specifies the buffer to retrieve the string. If NULL is specified, returns the size of the buffer enough to retrieve the string.

## Return Values

Returns TRUE if the current flag allows changes in EmEditor to be redrawn or prevents changes in EmEditor to be redrawn. Otherwise, returns FALSE.
