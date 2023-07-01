# EE\_REPLACE\_IN\_FILESW

在指定路径的多个文件中替换一个 Unicode 字符串。你能明确地发送该消息或用
[Editor\_ReplaceInFilesW](../macro/editor_replaceinfilesw) 或 [Editor\_BatchReplaceInFiles](../macro/editor_batchreplaceinfiles) 内联函数。

EE\_REPLACE\_IN\_FILESW

wParam = 0;

lParam = (LPARAM) (GREP\_INFO\_EX\*) pGrepInfo;

或

EE\_REPLACE\_IN\_FILESW

wParam = (WPARAM) (BATCH\_GREP\_INFO\*) pBatchGrepInfo;

lParam = (LPARAM) (FIND\_REPLACE\_INFO\*) pBatchArray;

## 参数

_pGrepInfo_

> 如果未指定批处理搜索，则此参数指定指针指向 [GREP\_INFO\_EX 结构](../structure/grep_info_ex) 或 [GREP\_INFOW 结构](../structure/grep_infow)。较新的插件应使用 [GREP\_INFO\_EX 结构](../structure/grep_info_ex)。

_pBatchGrepInfo_

> 如果指定了批处理搜索，则此参数指定指针指向 [BATCH\_GREP\_INFO 结构](../structure/batch_grep_info)。

_pBatchArray_

> 如果指定了批处理搜索，则此参数指定指针指向 [FIND\_REPLACE\_INFO 结构](../structure/find_replace_info) 的数组。

## 返回值

> 返回 FALSE 如果用户中止，不然，返回 TRUE。

## 支持版本

> 支持 EmEditor 4.02 或之后的版本。
