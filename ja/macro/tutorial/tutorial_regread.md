# レジストリを操作する ()

レジストリを操作するには、WshShell オブジェクトの RegRead メソッド、RegWrite メソッド、および RegDelete メソッドを利用することができます。

この例では、実行中のマクロのファイル名をレジストリから取得して表示します。

#### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

str = WshShell.RegRead( "HKCU\\\Software\\\EmSoft\\\EmEditor v3\\\Common\\\MacroFile"
);

alert( str );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

str = WshShell.RegRead( "HKCU\\Software\\EmSoft\\EmEditor v3\\Common\\MacroFile" )

alert str

## ヒント

JavaScript では、文字列内に「\\」を含めるには、「\\\」と記述する必要があります。

## 参考

)
