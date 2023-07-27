# EE\_FIND\_REPLACE

搜索或替换一个字符串。你能明确地发送该消息或用 [Editor\_FindReplace](../macro/editor_findreplace) 或 [Editor\_BatchFindReplace](../macro/editor_batchfindreplace) 内联函数。

EE\_FIND\_REPLACE

wParam = (WPARAM) (BATCH\_INFO\*) pBatchInfo;

lParam = (LPARAM) (FIND\_REPLACE\_INFO\*) pFindReplaceInfo;

## 参数

_pBatchInfo_

指针指向 [BATCH\_INFO 结构](../structure/batch_info)。此参数可以是 NULL 如果没有指定批次搜索。

_pFindReplaceInfo_

指针指向 [FIND\_REPLACE\_INFO 结构](../structure/find_replace_info)。如果 pBatchInfo 不是 NULL，此参数能指定 FIND\_REPLACE\_INFO 结构的数组。

## 返回值

如果找到搜索字符串，返回 S\_OK。如果找不到则返回 S\_FALSE。如果发生错误，返回值是负数。如果一个用户取消搜索，负数值包含 E\_ABORT，如果发生严重错误，返回 E\_FAIL。

## 版本

支持 Version 15.7 或之后的版本。
