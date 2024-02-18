# DeleteFile Method (Shell Object)

Deletes one or more specified files.

## 

### \[JavaScript\]

```
shell.DeleteFile( strFile );
```

### \[VBScript\]

```
shell.DeleteFile strFile
```

## Parameters

_strFile_

The name of the file to delete. It can contain wildard characters in the last path component.

## Examples

### \[JavaScript\]

```
shell.DeleteFile( "C:\\\\Test\\\\\*.txt" );
```

### \[VBScript\]

```
shell.DeleteFile "C:\\Test\\\*.txt"
```

## Version

Supported on EmEditor Professional Version 22.1 or later.
