# Editor\_ReplaceInFilesW

Replaces a Unicode string in multiple files in the specified location. You can
use this inline function or explicitly send the
[EE\_REPLACE\_IN\_FILESW](../message/ee_replace_in_filesw) message. This inline function is obsolete. Newer plug-ins should use the [Editor\_ReplaceInFiles inline function](editor_replaceinfiles) instead.

Editor\_ReplaceInFilesW( HWND hwnd, GREP\_INFOW pGrepInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pGrepInfo_

> Specifies a pointer to the [GREP\_INFOW \
> Structure](../structure/grep_infow).

## Return Value

> Returns FALSE if the user aborts, or TRUE if not.

## Version

> Supported on EmEditor Professional Version 4.02 or later.