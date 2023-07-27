# Editor\_GetStatusA

Retrieves the ANSI text displayed on the status bar. You can use this inline function
or explicitly send the [EE\_GET\_STATUSA \
message](../message/ee_get_statusa).

Editor\_GetStatusA( HWND hwnd, LPSTR szStatus, UINT nBufSize );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nBufSize_

Specifies the size of buffer in characters to retrieve the string, including
the terminating null character. You can specify 0 if _szStatus_ is
NULL. If the buffer size is not enough, _szStatus_ will retrieve no
string.

_szStatus_

Specifies the buffer to retrieve the string. If NULL is specified, returns
the size of the buffer enough to retrieve the string.

## Return Values

Returns the size of the buffer in characters enough to retrieve the string
including the terminating null character.
