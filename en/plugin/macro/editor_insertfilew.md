# Editor\_InsertFileW

Inserts the specified file contents at the cursor. The file name is specified
as a Unicode string. You can use this inline function or explicitly send the
[EE\_INSERT\_FILEW message](../message/ee_insert_filew).

Editor\_InsertFileW( HWND hwnd, LOAD\_FILE\_INFO\* pLoadFileInfo, LPCWSTR
szFileName );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pLoadFileInfo_

Pointer to a [LOAD\_FILE\_INFO](../structure/load_file_info) structure. If this parameter is NULL, Editor\_InsertFileW
will open a file by a method predefined by the properties.

_szFileName_

Specifies a full path file name. If a non-existing file is specified, Editor\_InsertFileW
will fail.

## Return Values

If the command is successful, the return value is nonzero. If the command
it not successful, the return value is zero.
