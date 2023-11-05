# EE\_REPLACE\_IN\_FILESW

Replaces a Unicode string in multiple files in the specified path. You can
send this message explicitly or use the
[Editor\_ReplaceInFilesW](../macro/editor_replaceinfilesw) or [Editor\_BatchReplaceInFiles](../macro/editor_batchreplaceinfiles) inline function.

```
EE_REPLACE_IN_FILESW
wParam = 0;
lParam = (LPARAM) (GREP_INFO_EX*) pGrepInfo;
or
EE_REPLACE_IN_FILESW
wParam = (WPARAM) (BATCH_GREP_INFO*) pBatchGrepInfo;
lParam = (LPARAM) (FIND_REPLACE_INFO*) pBatchArray;
```

## Parameters

_pGrepInfo_

If no batch search is specified, this parameter specifies a pointer to the [GREP\_INFO\_EX structure](../structure/grep_info_ex) or [GREP\_INFOW structure](../structure/grep_infow). Newer plug-ins should use the [GREP\_INFO\_EX structure](../structure/grep_info_ex).

_pBatchGrepInfo_

If a batch search is specified, this parameter specifies a pointer to the [BATCH\_GREP\_INFO structure](../structure/batch_grep_info).

_pBatchArray_

If a batch search is specified, this parameter specifies a pointer to the array of [FIND\_REPLACE\_INFO structures](../structure/find_replace_info).

## Return Value

Returns FALSE if the user aborts, or TRUE if not.

## Version

Supported on EmEditor Professional Version 4.02 or later.
