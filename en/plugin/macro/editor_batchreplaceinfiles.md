# Editor\_BatchReplaceInFiles

Replaces multiple strings in multiple files in the specified location. You can
use this inline function or explicitly send the
[EE\_REPLACE\_IN\_FILESW](../message/ee_replace_in_filesw) message.

Editor\_BatchReplaceInFiles( HWND hwnd, FIND\_REPLACE\_INFO\* pBatchArray, BATCH\_GREP\_INFO\* pGrepInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pBatchArray_

> Specifies a pointer to the array of [FIND\_REPLACE\_INFO structures](../structure/find_replace_info).

_pBatchGrepInfo_

> Specifies a pointer to the [BATCH\_GREP\_INFO structure](../structure/batch_grep_info).

## Return Value

> Returns FALSE if the user aborts, or TRUE if not.

## Version

> Supported on EmEditor Professional Version 15.7 or later.
