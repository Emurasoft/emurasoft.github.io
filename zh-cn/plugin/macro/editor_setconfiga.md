# Editor\_SetConfigA

变更为一个用 ANSI 字符串指定的配置。你能直接用该内联函数或明确地发送 [EE\_SET\_CONFIGA](../message/ee_set_configa) 消息。

Editor\_SetConfigA( HWND hwnd, LPCSTR szConfigName );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_szConfigName_

> 用 ANSI 字符串指定一个配置。

## 返回值

> 不使用返回值。