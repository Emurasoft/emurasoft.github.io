# Editor\_GetConfigA

将所选配置名称检索为 ANSI 字符串。你能直接用该内联函数或明确地发送 [EE\_GET\_CONFIGA](../message/ee_get_configa) 消息。

Editor\_GetConfigA( HWND hwnd, LPSTR szConfigName );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_szConfigName_

> 指定会接收配置名称的一个缓冲区。缓冲区大小必须至少是 MAX\_CONFIG\_NAME 所标示的以字节为单位的值。

## 返回值

> 不使用返回值。