# 显示一个消息框 (教程)

要在一个消息框中显示简单的文本，你能用 [alert \
方法](../window/window_alert) 或 [confirm 方法](../window/window_confirm)。然而，这些方法仅能显示三个按钮: YES，NO 以及 CANCEL。要在消息框中显示更多复杂的文本，请用 WshShell 对象的 Popup 方法。

下面的示例代码显示文本 Continue? 以及 YES，NO 和 CANCEL 按钮。变量 n 的数值是 6 如果选择了 YES 按钮，变为 7 如果选择了 NO 按钮，或 2 如果选择了 CANCEL 按钮。

## 

### \[JavaScript (JScript)\]

```
WshShell = new ActiveXObject( "WScript.Shell" );
n = WshShell.Popup( "Continue?", 0, "EmEditor", 3 );
```

### \[VBScript\]

```
Set WshShell = CreateObject( "WScript.Shell" )
n = WshShell.Popup( "Continue?", 0, "EmEditor", 3 )
```

## References

[Microsoft MSDN Library: Popup Method](https://docs.microsoft.com/en-us/previous-versions//x83z1d9f(v=vs.85))
