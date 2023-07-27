# EE\_REPLACE\_IN\_FILESA

Searches for an ANSI string from multiple files in the specified path. The
list of searched files will be displayed in the current window. If the current
document is modified, displays the prompt message box whether to save the
changes to the current file. You can send this message explicitly or use the
[Editor\_ReplaceInFilesA](../macro/editor_replaceinfilesa) inline function.

EE\_REPLACE\_IN\_FILESA

wParam = 0;

lParam = (LPARAM) (GREP\_INFOA) pGrepInfo;

## Parameters

_pGrepInfo_

Specifies a pointer to the [GREP\_INFOW \
Structure](../structure/grep_infow).

## Return Value

Returns FALSE if the user aborts, or TRUE if not.

## Version

Supported on EmEditor Professional Version 4.02 or later.
