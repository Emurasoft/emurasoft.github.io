# DeleteFolder Method (Shell Object)

Deletes one or more specified folders and their contents. The specified folder is deleted even if it is not empty.

#### \[JavaScript\]

shell. **DeleteFolder**( _strFolder_ );

#### \[VBScript\]

shell. **DeleteFolder** _strFolder_

## Parameters

_strFolder_

The name of the folder to delete. It can contain wildard characters in the last path component.

## Examples

#### \[JavaScript\]

shell.DeleteFolder( "C:\\\Test\\\folder" );

#### \[VBScript\]

shell.DeleteFolder "C:\\Test\\folder"

## Version

Supported on EmEditor Professional Version 22.1 or later.
