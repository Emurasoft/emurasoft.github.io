# Manipulate the Registry (Tutorial)

To manipulate the registry, use the RegRead Method, RegWrite Method, and RegDelete Method of WshShell Object.

The following example code reads the file name of a running macro from the registry, and displays it.

## 

### \[JavaScript (JScript)\]

```
WshShell = new ActiveXObject( "WScript.Shell" );
str = WshShell.RegRead( "HKCU\\\\Software\\\\EmSoft\\\\EmEditor v3\\\\Common\\\\MacroFile");
alert( str );
```

### \[VBScript\]

```
Set WshShell = CreateObject( "WScript.Shell" )
str = WshShell.RegRead( "HKCU\\Software\\EmSoft\\EmEditor v3\\Common\\MacroFile" )
alert str
```

## Tips:

In JavaScript, if you want to include a backslash "\\" within a string,
it must be preceded by another backslash "\\\\".

## References

[Microsoft MSDN Library: RegRead Method](https://docs.microsoft.com/en-us/previous-versions//x05fawxd(v=vs.85))
