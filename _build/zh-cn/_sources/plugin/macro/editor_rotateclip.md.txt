# Editor\_RotateClip

在剪贴板记录上旋转当前位置。你能直接用该内联函数或明确地发送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_RotateClip( HWND hwnd, int iDirection );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_iDirection_

> 指定你想要在剪贴板记录上旋转当前位置的方向。

## 返回值

> 如果成功的话，返回值是 1。如果消息失败，返回值是 -1。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。