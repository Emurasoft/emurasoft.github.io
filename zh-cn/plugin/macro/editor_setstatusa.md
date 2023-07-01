# Editor\_SetStatusA

在状态栏上显示一条 ANSI 消息。你能直接用该内联函数或明确地发送 [EE\_SET\_STATUSA](../message/ee_set_statusa) 消息。

Editor\_SetStatusA( HWND hwnd, LPCSTR szStatus );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_szStatus_

> 指定要显示在状态栏上的消息文本。

## 返回值

> 不使用返回值。
