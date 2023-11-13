# 运行外部程序 (教程)

要运行外部程序，请用 WshShell 对象的 Run 方法 。

下面的示例代码会运行 Windows 中的计算器并给它发送键击来执行一个简单的运算 1+2=。

## 

### \[JavaScript (JScript)\]

```
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
```

### \[JavaScript (V8)\]

```
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
```

### \[VBScript\]

```
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
```

## References

[Microsoft MSDN Library: Run Method](https://docs.microsoft.com/en-us/previous-versions//d5fk67ky(v=vs.85))
