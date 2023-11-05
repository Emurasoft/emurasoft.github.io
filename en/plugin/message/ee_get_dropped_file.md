# EE\_GET\_DROPPED\_FILE

Retrieves the most recently dropped file. You can send
this message explicitly or use the
[Editor\_GetDroppedFile](../macro/editor_getdroppedfile) inline function.

EE\_GET\_DROPPED\_FILE

wParam = (WPARAM) (int) nIndex;

lParam = (LPARAM) (LPWSTR) pszBuf;

## Parameters

_nIndex_

Specifies the index of the dropped file. A
zero-based index should be specified. If
-1 is specified, the total number of
the dropped files will be returned.

_pszBuf_

Specifies a buffer that will receive the dropped file
name. The buffer
size must be at least MAX\_PATH in
characters. This parameter can be NULL if -1 is
specified in nIndex.

## Return Values

The return value is nonzero if the dropped file exists for
the specified index. If -1 is specified in nIndex, the return value is the
total number of the dropped files.

## Version

Supported on EmEditor Version 8.00 or later.
