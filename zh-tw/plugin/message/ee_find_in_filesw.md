# EE\_FIND\_IN\_FILESW

在指定路徑的多個檔案中搜尋一個 Unicode 字符串。被搜尋的檔案列表會顯示在當前視窗內。如果當前文檔被修改，EmEditor 會顯示是否將更改保存到當前檔案的提示消息框。您能明確地發送該消息或用
[Editor\_FindInFilesW](../macro/editor_findinfilesw) 或 [Editor\_BatchFindInFiles](../macro/editor_batchfindinfiles) 內嵌函式。

EE\_FIND\_IN\_FILESW

wParam = 0;

lParam = (LPARAM) (GREP\_INFO\_EX\*) pGrepInfo;

或

EE\_FIND\_IN\_FILESW

wParam = (WPARAM) (BATCH\_GREP\_INFO\*) pBatchGrepInfo;

lParam = (LPARAM) (FIND\_REPLACE\_INFO\*) pBatchArray;

## 參數

_pGrepInfo_

> 如果未指定批次搜索，則此參數指定指針指向 [GREP\_INFO\_EX 結構](../structure/grep_info_ex) 或 [GREP\_INFOW 結構](../structure/grep_infow)。較新的外掛程式應使用 [GREP\_INFO\_EX 結構](../structure/grep_info_ex)。

_pBatchGrepInfo_

> 如果指定了批次搜索，則此參數指定指針指向 [BATCH\_GREP\_INFO 結構](../structure/batch_grep_info)。

_pBatchArray_

> 如果指定了批次搜索，則此參數指定指針指向 [FIND\_REPLACE\_INFO 結構](../structure/find_replace_info) 的陣列。

## 返回值

> 返回 FALSE，如果用戶中止，不然，返回 TRUE。

## 支持版本

> 支持 EmEditor 4.02 或之後的版本。
