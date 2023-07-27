# Editor\_Redraw

在 EmEditor 中允许或禁止重绘变更。你能直接用该内联函数或明确地发送
[EE\_REDRAW](../message/ee_redraw) 消息。

Editor\_Redraw( HWND hwnd, BOOL bRedraw );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_bRedraw_

指定重绘状态。如果该参数是 TRUE，内容会在发生变更之后被重绘。如果该参数是 FALSE，内容将不能在发生变更之后被重绘。

## 返回值

不使用返回值。
