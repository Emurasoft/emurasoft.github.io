# Editor\_OverwriteW

Inserts a Unicode string at the current cursor position. This overwrites the
existing string. You can use this inline function or explicitly send the
[EE\_INSERT\_STRINGW](../message/ee_insert_stringw)
message.

Editor\_OverwriteW( HWND hwnd, LPCWSTR szString, bool bKeepDestReturnType = false );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_szString_

> Specifies the string to be inserted.

_bKeepDestReturnType_

> Specifies that the destination return type (CR only, LF only or both CR and LF) should be kept. When this parameter is omitted, EmEditor keeps the return type specified in the szString parameter.

## Return Values

> The return value is not used.

## Version

> The bKeepDestReturnType flag is supported on EmEditor Version 7.00 or later.