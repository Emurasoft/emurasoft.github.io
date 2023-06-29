# GetFileAttributes Method

Returns the attributes of a specified file or folder.

#### \[JavaScript\]

nAttr = shell. **GetFileAttributes**( _strFile_ );

#### \[VBScript\]

nAttr = shell. **GetFileAttributes**( _strFile_ )

## Parameters

_strFile_

The full path and name of a file or folder to retrieve the attributes.

## Examples

#### \[JavaScript\]

nAttr = shell.GetFileAttributes( "C:\\\Test\\\file.txt" );

#### \[VBScript\]

nAttr = shell.GetFileAttributes( "C:\\Test\\file.txt" )

## Return Value

Returns a combination of the following values.

|     |     |
| --- | --- |
| Value | Description |
| 0 | Normal |
| 1 | Read-only |
| 2 | Hidden |
| 4 | System |
| 8 | Volume |
| 16 | Directory |
| 32 | Archive |
| 1024 | Alias |
| 2048 | Compressed |

## Version

Supported on EmEditor Professional Version 22.1 or later.