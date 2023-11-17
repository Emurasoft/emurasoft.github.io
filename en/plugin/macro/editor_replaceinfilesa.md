# Editor\_ReplaceInFilesA

Replaces an ANSI string in multiple files in the specified location. You can use this inline function or explicitly send the [EE\_REPLACE\_IN\_FILESA message](../message/ee_replace_in_filesa).

Editor\_ReplaceInFilesA( HWND hwnd, GREP\_INFOA pGrepInfo );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pGrepInfo_

Specifies a pointer to the [GREP\_INFOW Structure](../structure/grep_infow).

## Return Value

Returns FALSE if the user aborts, or TRUE if not.

## Version

Supported on EmEditor Professional Version 4.02 or later.
