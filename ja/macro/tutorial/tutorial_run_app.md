# 外部のアプリケーションを実行する ()

外部アプリケーションを実行するには、WshShell オブジェクトの Run メソッドを利用することができます。

この例では、電卓を実行して、1+2= という計算を実行します。

#### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

WshShell.Run( "calc.exe" );

Sleep( 1000 );

WshShell.SendKeys( "1" );

Sleep( 100 );

WshShell.SendKeys( "{+}" );

Sleep( 100 );

WshShell.SendKeys( "2" );

Sleep( 100 );

WshShell.SendKeys( "=" );

#### \[JavaScript (V8)\]

shell.Run( "calc.exe" );

Sleep( 1000 );

WshShell.SendKeys( "1" );

Sleep( 100 );

WshShell.SendKeys( "{+}" );

Sleep( 100 );

WshShell.SendKeys( "2" );

Sleep( 100 );

WshShell.SendKeys( "=" );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

WshShell.Run "calc.exe"

Sleep 1000

WshShell.SendKeys "1"

Sleep 100

WshShell.SendKeys "{+}"

Sleep 100

WshShell.SendKeys "2"

Sleep 100

WshShell.SendKeys "="

## 参考

)