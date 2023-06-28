# Editor\_BatchFindInFiles

在指定位置的多个文件中搜索多个字符串。搜索文件列表将显示在当前窗口中。如果当前文档被修改，则会出现一条消息提示，要求将变更保存到当前文件。你能直接用该内联函数或明确地发送 [EE\_FIND\_IN\_FILESW](../message/ee_find_in_filesw) 消息。

Editor\_BatchFindInFiles( HWND hwnd, FIND\_REPLACE\_INFO\* pBatchArray, BATCH\_GREP\_INFO\* pBatchGrepInfo );

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