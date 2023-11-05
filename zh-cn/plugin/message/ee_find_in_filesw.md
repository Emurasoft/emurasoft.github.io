# EE\_FIND\_IN\_FILESW

在指定路径的多个文件中搜索一个 Unicode 字符串。被搜索的文件列表会显示在当前窗口内。如果当前文档被修改，EmEditor 会显示是否将更改保存到当前文件的提示消息框。你能明确地发送该消息或用
[Editor\_FindInFilesW](../macro/editor_findinfilesw) 或 [Editor\_BatchFindInFiles](../macro/editor_batchfindinfiles) 内联函数。

```
EE_FIND_IN_FILESW
wParam = 0;
lParam = (LPARAM) (GREP_INFO_EX*) pGrepInfo;
或
EE_FIND_IN_FILESW
wParam = (WPARAM) (BATCH_GREP_INFO*) pBatchGrepInfo;
lParam = (LPARAM) (FIND_REPLACE_INFO*) pBatchArray;
```

## 参数

_pGrepInfo_

如果未指定批处理搜索，则此参数指定指针指向 [GREP\_INFO\_EX 结构](../structure/grep_info_ex) 或 [GREP\_INFOW 结构](../structure/grep_infow)。较新的插件应使用 [GREP\_INFO\_EX 结构](../structure/grep_info_ex)。

_pBatchGrepInfo_

如果指定了批处理搜索，则此参数指定指针指向 [BATCH\_GREP\_INFO 结构](../structure/batch_grep_info)。

_pBatchArray_

如果指定了批处理搜索，则此参数指定指针指向 [FIND\_REPLACE\_INFO 结构](../structure/find_replace_info) 的数组。

## 返回值

返回 FALSE，如果用户中止，不然，返回 TRUE。

## 支持版本

支持 EmEditor 4.02 或之后的版本。
