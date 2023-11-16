# Editor\_FindInFilesW

在指定路徑的多個檔案中搜尋一個 Unicode 字串。被搜尋的檔案清單會顯示在目前的視窗內。如果目前的文檔被修改，EmEditor 會顯示是否將更改儲存到目前的檔案的提示消息方塊。您能直接用該內嵌函式或明確地發送
[EE\_FIND\_IN\_FILESW](../message/ee_find_in_filesw) 消息。

Editor\_FindInFilesW( HWND hwnd, GREP\_INFOW pGrepInfo );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pGrepInfo_

指定一個指標至 [GREP\_INFOW 結構](../structure/grep_infow)。

## 返回值

返回 FALSE，如果使用者中止，不然，返回 TRUE。

## 支持版本

支持 EmEditor 4.02 或之後的版本。
