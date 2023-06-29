# Editor\_EditTemp

Creates temporary text as a new document. You can use this inline function or explicitly send the [EE\_EDIT\_TEMP](../message/ee_edit_temp)
message.

Editor\_EditTemp( HWND hwnd, LPCWSTR pszTempText, LPCWSTR pszTitle, LPCWSTR pszIconPath, LPCWSTR pszConfig, UINT nEncoding, POINT\_PTR\* pptInitialCaret = NULL, UINT nFlags = 0 );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pszTempText_

> Specifies temporary text on memory that you want to open as a new document.

_pszTitle_

> Specifies the title of the new document.

_pszIconPath_

> Specifies the path and file name of the icon that you want to use as a new document.

_pszConfig_

> Specifies the name of the configuration that the new document should use.

_nEncoding_

> Specifies the encoding of the file. The encoding constants are listed in ["EmEditor Macro Reference: Encoding Constants".](http://www.emeditor.org/en/macro_const_const_encoding.html)

_pptInitialCaret_

> Specifies the initial cursor position.

_nFlags_

> This value must be zero.

## Return Values

> The return value is the ID of the new document.

## Version

> Supported on EmEditor Version 9.00 or later.