# Editor\_BatchReplaceInFiles

在指定位置取代多個檔案中的多個字串。你能直接用該內嵌函式或明確地發送 [EE\_REPLACE\_IN\_FILESW](../message/ee_replace_in_filesw) 消息。

Editor\_BatchReplaceInFiles( HWND hwnd, FIND\_REPLACE\_INFO\* pBatchArray, BATCH\_GREP\_INFO\* pGrepInfo );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控點。

_pBatchArray_

> 指針指向 [FIND\_REPLACE\_INFO 結構](../structure/find_replace_info) 的陣列。

_pBatchGrepInfo_

> 指定指針指向 [BATCH\_GREP\_INFO 結構](../structure/batch_grep_info)。

## 返回值

> 如果使用者中止，返回 FALSE，否則返回 TRUE。

## 版本

> 指定 EmEditor Professional 20.0 或之後的版本。