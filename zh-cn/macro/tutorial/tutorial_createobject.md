# 创建对象 (教程)

这个章节介绍使用其他在 Windows 中可用的对象的简便方法。要使用对象，用 JavaScript (JScript) 中的 ActiveXObject 对象在或 VBScript 中的 CreateObject 函数。JavaScript (V8) 不支持此方法。

下面的例子用 WScript.Shell 对象来显示当前目录。

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
