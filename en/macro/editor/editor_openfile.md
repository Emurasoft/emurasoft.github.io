# OpenFile Method (Editor Object)

Opens an existing file.

## 

### \[JavaScript\]

```
editor.OpenFile( strFileName[, nEncoding[, nFlags]] );
```

### \[VBScript\]

```
editor.OpenFile strFileName[, nEncoding[, nFlags]]
```

## Parameters

_strFileName_

Specifies the full path and name of the file to be opened.

_nEncoding_

Selects from the **[Encoding Constants](../const/const_encoding)**,
or specify any encoding used in the Windows Operating System. If 0 is specified or omitted, this method will
open a file by an encoding predefined by the properties.

_nFlags_

Specifies a combination of the following values. If nEncoding is 0 or omitted, all values except eeOpenAllowNewWindow will be ignored.

|     |     |
| --- | --- |
| eeOpenAllowNewWindow | Opens as a new window if the current document is titled or modified. |
| eeOpenDetectUnicode | Detects Unicode signature (BOM). |
| eeOpenDetectUTF8 | Detects UTF-8. |
| eeOpenDetectCharset | Detects HTML/XML Charset. |
| eeOpenDetectAll | Detects all encodings. |
| eeUseDiskMode | Uses temporary files when opening a file. |
| eeDontUseDiskMode | Doesn't use temporary files when opening a file. If neither eeUseDiskMode nor eeDontUseDiskMode is specified, EmEditor automatically selects to use temporary files depending on the size of the file that is about to be opened. |

## Version

Supported on EmEditor Professional Version 4.00 or later. However, nEncoding and nFlags parameters can be omitted on Version 5.00 or later.
