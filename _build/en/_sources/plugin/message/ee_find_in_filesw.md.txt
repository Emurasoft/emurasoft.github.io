# EE\_FIND\_IN\_FILESW

Searches for an Unicode string from multiple files in the specified path. The
list of searched files will be displayed in the current window. If the current
document is modified, displays the prompt message box whether to save the
changes to the current file. You can send this message explicitly or use the
[Editor\_FindInFilesW](../macro/editor_findinfilesw) or [Editor\_BatchFindInFiles](../macro/editor_batchfindinfiles) inline function.

EE\_FIND\_IN\_FILESW

wParam = 0;

lParam = (LPARAM) (GREP\_INFO\_EX\*) pGrepInfo;

or

EE\_FIND\_IN\_FILESW

wParam = (WPARAM) (BATCH\_GREP\_INFO\*) pBatchGrepInfo;

lParam = (LPARAM) (FIND\_REPLACE\_INFO\*) pBatchArray;

## Parameters

_pGrepInfo_

> If no batch search is specified, this parameter specifies a pointer to the [GREP\_INFO\_EX structure](../structure/grep_info_ex) or [GREP\_INFOW structure](../structure/grep_infow). Newer plug-ins should use the [GREP\_INFO\_EX structure](../structure/grep_info_ex).

_pBatchGrepInfo_

> If a batch search is specified, this parameter specifies a pointer to the [BATCH\_GREP\_INFO structure](../structure/batch_grep_info).

_pBatchArray_

> If a batch search is specified, this parameter specifies a pointer to the array of [FIND\_REPLACE\_INFO structures](../structure/find_replace_info).

## Return Value

> Returns FALSE if the user aborts, or TRUE if not.

## Version

> Supported on EmEditor Professional Version 4.02 or later.