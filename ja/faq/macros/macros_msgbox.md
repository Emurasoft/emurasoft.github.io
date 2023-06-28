# Q. VBScript の MsgBox を使えないのですか?

残念ながら、MsgBox は使えません。その代わり、WshShell オブジェクトの Popup メソッドが利用できます。また、代わりに、 [**alert** メソッド](../../macro/window/window_alert) または [**confirm** メソッド](../../macro/window/window_confirm) を使用することもできます。

## 参考