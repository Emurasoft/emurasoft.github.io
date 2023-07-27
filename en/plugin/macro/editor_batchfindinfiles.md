# Editor\_BatchFindInFiles

Searches for multiple strings in multiple files in the specified location. The
list of searched files will be displayed in the current window. If the current
document is modified, a message prompt will ask to save the changes to the
current file. You can use this inline function or explicitly send the
[EE\_FIND\_IN\_FILESW](../message/ee_find_in_filesw) message.

Editor\_BatchFindInFiles( HWND hwnd, FIND\_REPLACE\_INFO\* pBatchArray, BATCH\_GREP\_INFO\* pBatchGrepInfo );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pBatchArray_

Specifies a pointer to the array of [FIND\_REPLACE\_INFO structures](../structure/find_replace_info).

_pBatchGrepInfo_

Specifies a pointer to the [BATCH\_GREP\_INFO structure](../structure/batch_grep_info).

## Return Value

Returns FALSE if the user aborts, or TRUE if not.

## Version

Supported on EmEditor Professional Version 20.0 or later.
