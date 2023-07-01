# Editor\_ReplaceInFilesW

在指定位置的多个文件中替换一个 Unicode 字符串。你能直接用该内联函数或明确地发送
[EE\_REPLACE\_IN\_FILESW](../message/ee_replace_in_filesw) 消息。

Editor\_ReplaceInFilesW( HWND hwnd, GREP\_INFOW pGrepInfo );

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
