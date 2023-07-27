# Editor\_ReplaceInFiles

在指定的多个文件中替换一个 Unicode 字符串。你能直接用该内联函数或明确地发送 [EE\_REPLACE\_IN\_FILESW](../message/ee_replace_in_filesw) 消息。

Editor\_ReplaceInFiles( HWND hwnd, GREP\_INFO\_EX\* pGrepInfo );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pGrepInfo_

指定一个指针指向 [GREP\_INFO\_EX 结构](../structure/grep_info_ex)。

## 返回值

返回 FALSE 如果用户终止，或 TRUE 如果没有终止。

## 版本

支持 Version 15.7 或之后的版本。
