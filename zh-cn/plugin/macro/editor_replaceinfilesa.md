# Editor\_ReplaceInFilesA

在指定位置的多个文件中搜索一个 ANSI 字符串。你能直接用该内联函数或明确地发送 [EE\_REPLACE\_IN\_FILESA message](../message/ee_replace_in_filesa).

Editor\_ReplaceInFilesA( HWND hwnd, GREP\_INFOA pGrepInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pGrepInfo_

> 指定一个指针指向 [GREP\_INFOW \
> 结构](../structure/grep_infow)。

## 返回值

> 返回 FALSE 如果用户中止，不然，返回 TRUE。

## 支持版本

> 支持 EmEditor 4.02 或之后的版本。
