# Editor\_GetActiveString

检索活动字符串。你能用这个内联函数或明确地发送 [EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) 消息。

Editor\_GetActiveString( HWND hwnd, ACTIVE\_STRING\_INFO\* pInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pTipInfo_

> 指针指向 [ACTIVE\_STRING\_INFO](../structure/active_string_info) 结构。

## 返回值

> 返回要检索包含终止 NULL 字符的活动字符串所需的缓冲区字符数。

## 版本

> 支持 EmEditor Professional 16.9 或之后的版本。
