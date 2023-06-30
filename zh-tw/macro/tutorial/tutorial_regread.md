# 操作注冊表 (�е{)

要操作注冊表，用 RegRead 方法，RegWrite 方法，和 WshShell 對象 的 RegDelete 方法。

下面的示例代碼會從注冊表上讀取一個運行的巨集的檔案名稱，并顯示它。

#### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

str = WshShell.RegRead( "HKCU\\\Software\\\EmSoft\\\EmEditor v3\\\Common\\\MacroFile"
);

alert( str );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

str = WshShell.RegRead( "HKCU\\Software\\EmSoft\\EmEditor v3\\Common\\MacroFile" )

alert str

## 提示:

在 JavaScript 中，如果您想要在一個字串中包括一個反斜杠 "\\"，它必須在前面加上另一個反斜杠 "\\\"。

## 參考

)