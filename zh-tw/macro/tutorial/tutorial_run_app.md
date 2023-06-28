# 運行外部程式

要運行外部程式，請用 WshShell 對象的 Run 方法 。

下面的示例代碼會運行 Windows 中的計算器并給它發送鍵擊來執行一個簡單的運算 1+2=。

#### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

WshShell.Run( "calc.exe" );

Sleep( 1000 );

wnd = shell.FindWindow( "", "Calculator" );

wnd.SetForeground();

shell.SendKeys( "1" );

Sleep( 100 );

shell.SendKeys( "{+}" );

Sleep( 100 );

shell.SendKeys( "2" );

Sleep( 100 );

shell.SendKeys( "=" );

#### \[JavaScript (V8)\]

shell.Run( "calc.exe" );

Sleep( 1000 );

wnd = shell.FindWindow( "", "Calculator" );

wnd.SetForeground();

shell.SendKeys( "1" );

Sleep( 100 );

shell.SendKeys( "{+}" );

Sleep( 100 );

shell.SendKeys( "2" );

Sleep( 100 );

shell.SendKeys( "=" );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

WshShell.Run "calc.exe"

Sleep 1000

wnd = shell.FindWindow( "", "Calculator" )

wnd.SetForeground

shell.SendKeys "1"

Sleep 100

shell.SendKeys "{+}"

Sleep 100

shell.SendKeys "2"

Sleep 100

shell.SendKeys "="

## References

)