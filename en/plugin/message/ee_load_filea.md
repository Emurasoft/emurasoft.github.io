# EE\_LOAD\_FILEA

Loads a specified file into EmEditor. The file name is specified by an ANSI
string. You can send this message explicitly or use the
[Editor\_LoadFileA](../macro/editor_loadfilea) inline function.

```
EE_LOAD_FILEA
wParam = (WPARAM) (LOAD_FILE_INFO_EX*) pLoadFileInfo;
lParam = (LPARAM) (LPCSTR) szFileName;
```

## Parameters

_pLoadFileInfo_

Pointer to a [LOAD\_FILE\_INFO\_EX](../structure/load_file_info) structure. If this parameter is NULL, EE\_LOAD\_FILEA will
open a file by a method predefined by the properties.

_szFileName_

Specifies a full path file name in bytes. If a non-existing file is
specified, EE\_LOAD\_FILEA will fail.

## Return Values

If the command is enable, the return value is nonzero. If the command it
not enable, the return value is zero.
