# Editor\_SaveFileA

儲存文字到一個指定的檔案中。檔案名稱被指定為一個 ANSI 字串。您能直接用該內嵌函式或明確地發送
[EE\_SAVE\_FILEA](../message/ee_save_filea) 消息。

Editor\_SaveFileA( HWND hwnd, BOOL bReplace, LPSTR szFileName );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_bReplace_

> 指定 TRUE 如果文字用一個指定的名稱儲存，并且 EmEditor 保留該檔案名。另外，顯示在 EmEditor 視窗上的標題也會被改變。指定 FALSE 如果儲存了該文字的副本，并且 EmEditor 所保留的檔案名稱將不會被改變。

_szFileName_

> 用位元指定一個完整的路徑檔案名稱。

## 返回值

> 如果消息成功，返回值不是零。如果消息不成功，返回值是零。