# オブジェクトを作成する (チュートリアル)

このセクションでは、Windows
で利用できる他のオブジェクトを利用した便利な使い方紹介します。オブジェクトを利用できるように作成するためには、JavaScript (JScript) では、ActiveXObject
オブジェクトを利用することができます。一方、VBScript では、CreateObject 関数が利用できます。JavaScript (V8) では、この方法はサポートされていません。

この例では、WScript.Shell というオブジェクトを利用し、カレント ディレクトリを表示します。

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

## 参考

[ActiveXObject Object (JavaScript)](https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/scripting-articles/7sw4ddf8%28v=vs.84%29)

[Microsoft MSDN Library: CreateObject Function (VBScript)](https://docs.microsoft.com/en-us/previous-versions//dcw63t7z%28v=vs.85%29)
