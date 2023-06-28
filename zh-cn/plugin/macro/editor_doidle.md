# Editor\_DoIdle

刷新工具栏，窗口标题，标签页及其他。你能直接用该内联函数或明确地发送 [EE\_DO\_IDLE](../message/ee_do_idle) 消息。

Editor\_DoIdle( HWND hwnd, BOOL bResetTab );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_bResetTab_

> 刷新标签页。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 5.00 或之后的版本。