# Editor\_UpdateToolbar

在工具栏中更新一个按钮的状态。你能直接用该内联函数或明确地发送 [EE\_UPDATE\_TOOLBAR](../message/ee_update_toolbar) 消息。

Editor\_UpdateToolbar( HWND hwnd, UINT nCmdID );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nCmdID_

指定插件的实例句柄。

## 返回值

不使用返回值。
