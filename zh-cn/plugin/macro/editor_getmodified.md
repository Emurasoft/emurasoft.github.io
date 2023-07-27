# Editor\_GetModified

检索文本的修改状态。你能直接用该内联函数或明确地发送 [EE\_GET\_MODIFIED](../message/ee_get_modified) 消息。

Editor\_GetModified( HWND hwnd );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

## 返回值

如果文本被修改，返回值是 TRUE。如果文本没有被修改，返回值是 FALSE。
