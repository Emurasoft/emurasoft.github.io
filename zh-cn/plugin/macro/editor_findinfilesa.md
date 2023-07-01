# Editor\_FindInFilesA

在指定路径的多个文件中搜索一个 ANSI 字符串。被搜索的文件列表会显示在当前窗口内。如果当前文档被修改，EmEditor 会显示是否将更改保存到当前文件的提示消息框。你能直接用该内联函数或明确地发送
[EE\_FIND\_IN\_FILESA](../message/ee_find_in_filesa) 消息。

Editor\_FindInFilesA( HWND hwnd, GREP\_INFOA pGrepInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pGrepInfo_

> 指定一个指针指向 [GREP\_INFOA \
> 结构](../structure/grep_infoa)。

## 返回值

> 返回 FALSE，如果用户中止，不然，返回 TRUE。

## 支持版本

> 支持 EmEditor 4.02 或之后的版本。
