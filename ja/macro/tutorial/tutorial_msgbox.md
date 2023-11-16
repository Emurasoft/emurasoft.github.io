# メッセージを表示する (チュートリアル)

簡単なメッセージを表示するには、 [alert メソッド](../window/window_alert) や [confirm メソッド](../window/window_confirm) が利用できます。しかし、これらのメソッドでは、\[はい\]、\[いいえ\]、および
\[キャンセル\] の 3 個のボタンを表示することができません。このように、さらに複雑なメッセージ ボックスを表示するには、WshShell オブジェクトの Popup メソッドを利用することができます。

この例では、「Continue?」というメッセージを表示し、\[はい\]、\[いいえ\]、および \[キャンセル\] の 3 個のボタンを表示します。\[はい\]
ボタンが選択されると 6 が \[いいえ\] ボタンが選択されると 7 が、\[キャンセル\] ボタンが選択されると 2 が変数 n に代入されます。

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

## 参考

[Microsoft MSDN Library: Popup Method](https://docs.microsoft.com/en-us/previous-versions//x83z1d9f(v=vs.85))
