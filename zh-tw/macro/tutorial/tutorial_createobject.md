# 創建對象 (�е{)

這個章節介紹使用其他在 Windows 中可用的對象的簡便方法。要使用對象，用 JavaScript (JScript) 中的 ActiveXObject 對象在或 VBScript 中的 CreateObject 函數。JavaScript (V8) 不支持此方法。

下面的例子用 WScript.Shell 對象來顯示目前的目錄。

#### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

alert( WshShell.CurrentDirectory );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

alert WshShell.CurrentDirectory

## 參考
