# EE\_FIND\_REPLACE

搜索或取代一個字串。你能明確地發送該消息或用 [Editor\_FindReplace](../macro/editor_findreplace) 或 [Editor\_BatchFindReplace](../macro/editor_batchfindreplace) 內嵌函式。

EE\_FIND\_REPLACE

wParam = (WPARAM) (BATCH\_INFO\*) pBatchInfo;

lParam = (LPARAM) (FIND\_REPLACE\_INFO\*) pFindReplaceInfo;

## 參數

_pBatchInfo_

指針指向 [BATCH\_INFO 結構](../structure/batch_info)。此參數可以是 NULL 如果沒有指定批次搜索。

_pFindReplaceInfo_

指針指向 [FIND\_REPLACE\_INFO 結構](../structure/find_replace_info)。如果 pBatchInfo 不是 NULL，此參數能指定 FIND\_REPLACE\_INFO 結構的陣列。

## 返回值

如果找到搜索字串，返回 S\_OK。如果找不到則返回 S\_FALSE。如果發生錯誤，返回值是負數。如果一個使用者取消搜索，負數值包含 E\_ABORT，如果發生嚴重錯誤，返回 E\_FAIL。

## 版本

支持 Version 15.7 或之後的版本。
