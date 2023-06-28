# Editor\_SetClipPos

在剪贴板记录上设置当前位置。你能直接用该内联函数或明确地发送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_SetClipPos( HWND hwnd, int iPos );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_iPos_

> 在剪贴板记录上指定新位置。

## 返回值

> 在剪贴板记录上检索当前位置。如果消息失败，返回值是 -1。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。