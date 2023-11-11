# 顯示一個消息方塊 (教程)

要在一個消息方塊中顯示簡單的文字，您能用 [alert \
方法](../window/window_alert) 或 [confirm 方法](../window/window_confirm)。然而，這些方法僅能顯示三個按鈕: YES，NO 以及 CANCEL。要在消息方塊中顯示更多復雜的文字，請用 WshShell 對象的 Popup 方法。

下面的示例代碼顯示文字 Continue? 以及 YES，NO 和 CANCEL 按鈕。變量 n 的數值是 6 如果選擇了 YES 按鈕，變為 7 如果選擇了 NO 按鈕，或 2 如果選擇了 CANCEL 按鈕。

## 

### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

n = WshShell.Popup( "Continue?", 0, "EmEditor", 3 );

### \[VBScript\]

```
Set WshShell = CreateObject( "WScript.Shell" )
n = WshShell.Popup( "Continue?", 0, "EmEditor", 3 )
```

## References

[Microsoft MSDN Library: Popup Method](https://docs.microsoft.com/en-us/previous-versions//x83z1d9f(v=vs.85))
