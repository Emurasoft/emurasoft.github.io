# InsertFromFile Method (Selection Object)

Inserts the contents of the specified file at the cursor position.

## 

### \[JavaScript\]

```
document.selection.InsertFromFile( strFileName, nEncoding, nFlags );
```

### \[VBScript\]

```
document.selection.InsertFromFile strFileName, nEncoding, nFlags
```

## Parameters

_strFileName_

Specifies the full path and name of the file to be opened.

_nEncoding_

Selects from the [Encoding Constants](../const/const_encoding), or specify any code page used in the Windows Operating System.

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeOpenDetectUnicode | Detects Unicode signature (BOM). |
| eeOpenDetectUTF8 | Detects UTF-8. |
| eeOpenDetectCharset | Detects HTML/XML Charset. |
| eeOpenDetectAll | Detects all encodings. |

## Version

Supported on EmEditor Professional Version 4.00 or later.
