# Editor\_LoadFileW

Loads a specified file into EmEditor. The file name is specified as a Unicode
string. You can use this inline function or explicitly send the
[EE\_LOAD\_FILEW](../message/ee_load_filew) message.

Editor\_LoadFileW( HWND hwnd, LOAD\_FILE\_INFO\_EX\* pLoadFileInfo, LPCWSTR szFileName
);

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pLoadFileInfo_

Pointer to a [LOAD\_FILE\_INFO\_EX](../structure/load_file_info) structure. If this parameter is NULL, Editor\_LoadFileW will
open a file by a method predefined by the properties.

_szFileName_

Specifies a full path file name in bytes. If a non-existing file is
specified, Editor\_LoadFileW will fail.

## Return Values

If the command is enable, the return value is nonzero. If the command it
not enable, the return value is zero.
