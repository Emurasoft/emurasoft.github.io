# Editor\_KeyboardProp

显示指定命令 ID 和配置的键盘属性。你能直接用该内联函数或明确地发送 [EE\_KEYBOARD\_PROP](../message/ee_keyboard_prop) 消息。

Editor\_KeyboardProp( HWND hwnd, UINT nCmdID, LPCWSTR pszConfigName );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nCmdID_

> 给键盘属性上的初始选区指定命令 ID。

_pszConfigName_

> 指定 EmEditor 显示键盘属性的配置。

## 返回值

> 如果用户在配置属性上选择 OK，返回值是 TRUE。如果用户选择 Cancel，返回值是 FALSE。
