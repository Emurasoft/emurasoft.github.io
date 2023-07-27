# Editor\_SetModified

变更文本的修改状态。你能直接用该内联函数或明确地发送 [EE\_SET\_MODIFIED](../message/ee_set_modified) 消息。

Editor\_SetModified( HWND hwnd, BOOL bModified );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_bModified_

TRUE，把状态变更为修改过，或 FALSE，把状态变更为未经修改。

## 返回值

不使用返回值。
