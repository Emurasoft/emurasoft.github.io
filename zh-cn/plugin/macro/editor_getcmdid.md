# Editor\_GetCmdID

获得插件命令 ID。你能直接用该内联函数或明确地发送 [EE\_GET\_CMD\_ID](../message/ee_get_cmd_id)
消息。

Editor\_GetCmdID( HWND hwnd, HINSTANCE hInstance );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_hInstance_

指定插件的实例句柄。

## 返回值

返回命令 ID 来运行该插件。
