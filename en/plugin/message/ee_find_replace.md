# EE\_FIND\_REPLACE

Searches or replaces a string. You can send this message
explicitly or use the [Editor\_FindReplace](../macro/editor_findreplace) or [Editor\_BatchFindReplace](../macro/editor_batchfindreplace) inline function.

EE\_FIND\_REPLACE

wParam = (WPARAM) (BATCH\_INFO\*) pBatchInfo;

lParam = (LPARAM) (FIND\_REPLACE\_INFO\*) pFindReplaceInfo;

## Parameters

_pBatchInfo_

Pointer to the [BATCH\_INFO structure](../structure/batch_info). This parameter can be NULL if no batch search is specified.

_pFindReplaceInfo_

Pointer to the [FIND\_REPLACE\_INFO structure](../structure/find_replace_info). If pBatchInfo is not NULL, this parameter can specify the array of FIND\_REPLACE\_INFO structures.

## Return Values

Returns S\_OK if the searched string is found, S\_FALSE if not found. The return value is a negative value if an error occurs. The negative value includes E\_ABORT if a user cancels the search, and E\_FAIL if a fatal error occurs.

## Version

Supported on Version 15.7 or later.
