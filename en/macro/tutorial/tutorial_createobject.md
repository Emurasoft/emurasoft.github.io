# Creates Object (Tutorial)

This section introduces convenient ways of using other Objects available in Windows.
To use Objects, use the ActiveXObject Object in JavaScript (JScript) or CreateObject function in VBScript. JavaScript (V8) does not support this method.

The following example uses WScript.Shell Object to display the current directory.

#### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

alert( WshShell.CurrentDirectory );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

alert WshShell.CurrentDirectory

## References