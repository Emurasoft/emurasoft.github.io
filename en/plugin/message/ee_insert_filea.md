# EE\_INSERT\_FILEA

Inserts the specified file contents at the cursor. The file name is specified
as an ANSI string. You can send this message explicitly or use the
[Editor\_InsertFileA](../macro/editor_insertfilea) inline function.

```
EE_INSERT_FILEA
wParam = (WPARAM) (LOAD_FILE_INFO*) pLoadFileInfo;
lParam = (LPARAM) (LPCSTR) szFileName;
```

## Parameters

_pLoadFileInfo_

Pointer to a [LOAD\_FILE\_INFO](../structure/load_file_info) structure. If this parameter is NULL, EE\_INSERT\_FILEA will
open a file by a method predefined by the properties.

_szFileName_

Specifies a full path file name. If a non-existing file is specified, EE\_INSERT\_FILEA
will fail.

## Return Values

If the command is successful, the return value is nonzero. If the command
it not successful, the return value is zero.
