# FileExists Method (Shell Object)

Returns true if a specified file exists; false if it does not.

## 

### \[JavaScript\]

```
b = shell.FileExists( strFile );
```

### \[VBScript\]

```
b = shell.FileExists( strFile )
```

## Parameters

_strFile_

The name of the file whose existance is to be determined.

## Examples

### \[JavaScript\]

```
b = shell.FileExists( "C:\\\\Test\\\\file.txt" );
```

### \[VBScript\]

```
b = shell.FileExists( "C:\\Test\\file.txt" )
```

## Version

Supported on EmEditor Professional Version 22.1 or later.
