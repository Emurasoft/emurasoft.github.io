# Editor\_FindInFilesA

Searches for an ANSI string in multiple files in the specified location. The
list of searched files will be displayed in the current window. If the current
document is modified, a message prompt will ask to save the
changes to the current file. You can use this inline function or explicitly send the
[EE\_FIND\_IN\_FILESA](../message/ee_find_in_filesa) message.

Editor\_FindInFilesA( HWND hwnd, GREP\_INFOA pGrepInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pGrepInfo_

> Specifies a pointer to the [GREP\_INFOA \
> Structure](../structure/grep_infoa).

## Return Value

> Returns FALSE if the user aborts, or TRUE if not.

## Version

> Supported on EmEditor Professional Version 4.02 or later.
