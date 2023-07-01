# Editor\_ReplaceInFiles

Replaces a Unicode string in multiple files in the specified location. You can
use this inline function or explicitly send the
[EE\_REPLACE\_IN\_FILESW](../message/ee_replace_in_filesw) message.

Editor\_ReplaceInFiles( HWND hwnd, GREP\_INFO\_EX\* pGrepInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pGrepInfo_

> Specifies a pointer to the [GREP\_INFO\_EX \
> Structure](../structure/grep_info_ex).

## Return Value

> Returns FALSE if the user aborts, or TRUE if not.

## Version

> Supported on EmEditor Professional Version 15.7 or later.
