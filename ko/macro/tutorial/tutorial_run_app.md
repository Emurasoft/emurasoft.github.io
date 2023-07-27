# 외부 응용 프로그램 실행 (Ʃ�丮��)

외부 응용 프로그램을 실행하려면, WshShell 개체의 Run 메서드를 사용합니다.

다음의 예제 코드는 Windows 계산기를 실행하고 1+2=의 간단한 계산을 실행하는 키 입력을 전송합니다.

## 

### \[JavaScript\]

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

## 참조:
