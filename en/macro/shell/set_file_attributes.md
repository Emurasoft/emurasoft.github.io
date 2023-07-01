# SetFileAttributes Method (Shell Object)

Sets the attributes of a specified file or folder.

#### \[JavaScript\]

shell. **SetFileAttributes**( _strFile_, _nAttr_ );

#### \[VBScript\]

shell. **SetFileAttributes** _strFile_, _nAttr_

## Parameters

_strFile_

The full path and name of a file or folder to set the attributes.

_nAttr_

A combination of the following values.

|     |     |
| --- | --- |
| Value | Description |
| 0 | Normal |
| 1 | Read-only |
| 2 | Hidden |
| 4 | System |
| 32 | Archive |

## Examples

#### \[JavaScript\]

shell.SetFileAttributes( "C:\\\Test\\\file.txt", 1 );

#### \[VBScript\]

shell.SetFileAttributes "C:\\Test\\file.txt", 1

## Version

Supported on EmEditor Professional Version 22.1 or later.
