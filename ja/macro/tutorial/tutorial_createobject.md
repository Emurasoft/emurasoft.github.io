# オブジェクトを作成する ()

このセクションでは、Windows
で利用できる他のオブジェクトを利用した便利な使い方紹介します。オブジェクトを利用できるように作成するためには、JavaScript (JScript) では、ActiveXObject
オブジェクトを利用することができます。一方、VBScript では、CreateObject 関数が利用できます。JavaScript (V8) では、この方法はサポートされていません。

この例では、WScript.Shell というオブジェクトを利用し、カレント ディレクトリを表示します。

#### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

alert( WshShell.CurrentDirectory );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

alert WshShell.CurrentDirectory

## 参考
