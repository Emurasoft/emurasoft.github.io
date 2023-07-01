# Editor\_LoadConfigA

重新载入由一个 ANSI 字符串指定名称的配置。你能直接用该内联函数或明确地发送 [EE\_LOAD\_CONFIGA](../message/ee_load_configa) 消息。

Editor\_LoadConfigA( HWND hwnd, LPCSTR szConfigName );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_szConfigName_

> 指定要重新载入的配置名称。

## 返回值

> 不使用返回值。
