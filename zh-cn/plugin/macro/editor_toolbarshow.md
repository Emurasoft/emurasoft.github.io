# Editor\_ToolbarShow

显示或隐藏一个自定义工具栏。你能直接用该内联函数或明确地发送 [EE\_TOOLBAR\_SHOW](../message/ee_toolbar_show)
消息。

Editor\_ToolbarShow( HWND hwnd, UINT nCustomRebarID, BOOL bVisible );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nToolbarID_

指定要关闭的工具栏。这会是 EE\_TOOLBAR\_OPEN 消息的返回值。

_bVisible_

指定 TRUE 如果要显示工具栏，或 FALSE，如果要隐藏工具栏。

## 返回值

如果消息成功并且工具栏状态被改变，返回值是 TRUE。如果消息不成功或工具栏状态没有更改，返回值是 FALSE。

## 支持版本

支持 EmEditor 7.00 或之后的版本。
