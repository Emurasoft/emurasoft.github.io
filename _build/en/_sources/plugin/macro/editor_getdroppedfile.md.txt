# Editor\_GetDroppedFile

Retrieves the most recently dropped file. You can use this inline function or explicitly send the [EE\_GET\_DROPPED\_FILE](../message/ee_get_dropped_file)
message.

Editor\_GetDroppedFile( HWND hwnd, int nIndex, LPWSTR pszBuf );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nIndex_

> Specifies the index of the dropped file. A zero-based index should be specified. If -1 is specified, the total number of the dropped files will be returned.

_pszBuf_

> Specifies a buffer that will receive the dropped file name. The buffer size must be at least MAX\_PATH in characters. This parameter can be NULL if -1 is specified in nIndex.

## Return Values

> The return value is nonzero if the dropped file exists for
> the specified index. If -1 is specified in nIndex, the return value is the
> total number of the dropped files.

## Version

> Supported on EmEditor Version 8.00 or later.