# Editor\_DocSaveFileW

儲存指定文檔中的文字到另一個指定的檔案中。檔案名稱被指定為一個 Unicode 字串。您能直接用該內嵌函式或明確地發送
[EE\_SAVE\_FILEW](../message/ee_save_filew) 消息。

Editor\_SaveFileW( HWND hwnd, int iDoc, BOOL bReplace, LPWSTR szFileName );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_iDoc_

> 指定目標文檔的索引。如果指定值為 -1，目前的活動文檔會被設為目標文檔。

_bReplace_

> 指定 TRUE 如果文字用一個指定的名稱儲存，并且 EmEditor 保留該檔案名。另外，顯示在 EmEditor 視窗上的標題也會被改變。指定 FALSE 如果儲存了該文字的副本，并且 EmEditor 所保留的檔案名稱將不會被改變。

_szFileName_

> 用位元指定一個完整的路徑檔案名稱。

## 返回值

> 如果消息成功，返回值不是零。如果消息不成功，返回值是零。

## 支持版本

> 支持 EmEditor 5.00 或之後的版本。