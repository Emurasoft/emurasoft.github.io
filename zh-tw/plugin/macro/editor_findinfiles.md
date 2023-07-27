# Editor\_FindInFiles

在指定的多個檔案中搜索一個 Unicode 字串。被搜索的檔案清單會顯示在目前的視窗中。如果目前的文檔被更改了，會出現一條即時消息詢問你是否要儲存變更到目前的檔案中。你能直接用該內嵌函式或明確地發送
[EE\_FIND\_IN\_FILESW](../message/ee_find_in_filesw) 消息。

Editor\_FindInFiles( HWND hwnd, GREP\_INFO\_EX\* pGrepInfo );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pGrepInfo_

指定一個指針指向 [GREP\_INFO\_EX 結構](../structure/grep_info_ex)。

## 返回值

返回 FALSE 如果使用者終止，或 TRUE 如果沒有終止。

## 版本

支持 Version 15.7 或之後的版本。
