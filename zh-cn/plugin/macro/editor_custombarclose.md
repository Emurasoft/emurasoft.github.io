# Editor\_CustomBarClose

关闭自定义分栏。你能直接用该内联函数或明确地发送 [EE\_CUSTOM\_BAR\_CLOSE](../message/ee_custom_bar_close) 消息。

Editor\_CustomBarClose( HWND hwnd, UINT nCustomBarID );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nCustomBarID_

> 指定要关闭的自定义分栏。这会是 Editor\_CustomBarOpen 内联函数的返回值。

## 返回值

> 如果消息成功，返回值为非零值。如果该消息不成功，返回值为零。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。
