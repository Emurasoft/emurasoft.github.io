# EE\_INSERT\_FILEW

Inserts the specified file contents at the cursor. The file name is specified
as a Unicode string. You can send this message explicitly or use the
[Editor\_InsertFileW](../macro/editor_insertfilew) inline function.

EE\_INSERT\_FILEW

wParam = (WPARAM) (LOAD\_FILE\_INFO\*) pLoadFileInfo;

lParam = (LPARAM) (LPCWSTR) szFileName;

## Parameters

_pLoadFileInfo_

> Pointer to a [LOAD\_FILE\_INFO](../structure/load_file_info) structure. If this parameter is NULL, EE\_INSERT\_FILEW will
> open a file by a method predefined by the properties.

_szFileName_

> Specifies a full path file name. If a non-existing file is specified, EE\_INSERT\_FILEW
> will fail.

## Return Values

> If the command is successful, the return value is nonzero. If the command
> it not successful, the return value is zero.