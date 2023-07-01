# Editor\_ToolbarOpen

打开自定义工具栏。你能直接用该内联函数或明确地发送 [EE\_TOOLBAR\_OPEN](../message/ee_toolbar_open)
消息。

Editor\_ToolbarOpen( HWND hwnd, TOOLBAR\_INFO\* pToolbarInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pToolbarInfo_

> 指针指向 TOOLBAR\_INFO 结构。

## 返回值

> 返回值是一个自定义工具栏 ID。如果消息失败，返回值为零。

## 支持版本

> 支持 EmEditor 7.00 或之后的版本。
