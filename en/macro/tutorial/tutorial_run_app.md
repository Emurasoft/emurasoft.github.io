# Run External Applications (Tutorial)

To run an external application, use the Run Method of WshShell Object.

The following example code runs the Windows calculator and sends it keystrokes to execute a simple calculation 1+2=.

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
