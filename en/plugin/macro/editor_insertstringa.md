# Editor\_InsertStringA

Inserts an ANSI string into the current cursor position. This may overwrite
the existing string depending on the current Properties. You can use this inline function or explicitly send the [EE\_INSERT\_STRINGA](../message/ee_insert_stringa) message.

Editor\_InsertStringA( HWND hwnd, LPCSTR szString, bool bKeepDestReturnType = false );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_szString_

> Specifies the string to be inserted.

_bKeepDestReturnType_

> Specifies that the destination return type (CR only, LF only or both CR and LF) should be kept. When this parameter is omitted, EmEditor keeps the return type specified in the szString parameter.

## Return Values

> The return value is not used.