# Editor\_BatchReplaceInFiles

在指定位置替换多个文件中的多个字符串。你能直接用该内联函数或明确地发送 [EE\_REPLACE\_IN\_FILESW](../message/ee_replace_in_filesw) 消息。

Editor\_BatchReplaceInFiles( HWND hwnd, FIND\_REPLACE\_INFO\* pBatchArray, BATCH\_GREP\_INFO\* pGrepInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pBatchArray_

> 指针指向 [FIND\_REPLACE\_INFO 结构](../structure/find_replace_info) 的数组。

_pBatchGrepInfo_

> 指定指针指向 [BATCH\_GREP\_INFO 结构](../structure/batch_grep_info)。

## 返回值

> 如果用户中止，返回 FALSE，否则返回 TRUE。

## 版本

> 指定 EmEditor Professional 20.0 或之后的版本。
