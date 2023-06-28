# EE\_REPLACE\_IN\_FILESA

从指定路径的多个文件中搜索一个 ANSI 字符串。被搜索的文件列表会在当前窗口中显示。如果当前文档被修改，会显示是否将更改保存到当前文件的提示消息框。你能明确地发送该消息或用
[Editor\_ReplaceInFilesA](../macro/editor_replaceinfilesa) 内联函数。

EE\_REPLACE\_IN\_FILESA

wParam = 0;

lParam = (LPARAM) (GREP\_INFOA) pGrepInfo;

## 参数

_pGrepInfo_

> 指定一个指针指向 [GREP\_INFOW \
> 结构](../structure/grep_infow)。

## 返回值

> 返回 FALSE 如果用户中止，不然，返回 TRUE。

## 支持版本

> 支持 EmEditor 4.02 或之后的版本。