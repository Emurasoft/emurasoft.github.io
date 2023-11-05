# EE\_LOAD\_FILEW

Loads a specified file into EmEditor. The file name is specified by an ANSI
string. You can send this message explicitly or use the
[Editor\_LoadFileW](../macro/editor_loadfilew) inline function.

```
EE_LOAD_FILEW
wParam = (WPARAM) (LOAD_FILE_INFO_EX*) pLoadFileInfo;
lParam = (LPARAM) (LPCWSTR) szFileName;
```

## Parameters

_pLoadFileInfo_

Pointer to a [LOAD\_FILE\_INFO\_EX](../structure/load_file_info) structure. If this parameter is NULL, EE\_LOAD\_FILEW will
open a file by a method predefined by the properties.

_szFileName_

Specifies a full path file name in bytes. If a non-existing file is
specified, EE\_LOAD\_FILEW will fail.

## Return Values

If the command is enable, the return value is nonzero. If the command it
not enable, the return value is zero.
