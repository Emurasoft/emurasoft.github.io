# Creates Object (Tutorial)

This section introduces convenient ways of using other Objects available in Windows.
To use Objects, use the ActiveXObject Object in JavaScript (JScript) or CreateObject function in VBScript. JavaScript (V8) does not support this method.

The following example uses WScript.Shell Object to display the current directory.

## 

### \[JavaScript (JScript)\]

```
WshShell = new ActiveXObject( "WScript.Shell" );
alert( WshShell.CurrentDirectory );
```

### \[VBScript\]

```
Set WshShell = CreateObject( "WScript.Shell" )
alert WshShell.CurrentDirectory
```

## References

[ActiveXObject Object (JavaScript)](https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/scripting-articles/7sw4ddf8%28v=vs.84%29)

[Microsoft MSDN Library: CreateObject Function (VBScript)](https://docs.microsoft.com/en-us/previous-versions//dcw63t7z%28v=vs.85%29)
