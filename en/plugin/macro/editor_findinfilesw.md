# Editor\_FindInFilesW

Searches for a Unicode string in multiple files in the specified location. The
list of searched files will be displayed in the current window. If the current
document is modified, a message prompt will ask to save the changes to the
current file. This inline function is obsolete. Newer plug-ins should use the [Editor\_FindInFiles inline function](editor_findinfiles) instead. You can use this inline function or explicitly send the
[EE\_FIND\_IN\_FILESW](../message/ee_find_in_filesw) message.

Editor\_FindInFilesW( HWND hwnd, GREP\_INFOW pGrepInfo );

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
