# Editor\_GetStatusA

检索显示在状态栏上的 ANSI 文本。你能直接用该内联函数或明确地发送 [EE\_GET\_STATUSA 消息](../message/ee_get_statusa)。

Editor\_GetStatusA( HWND hwnd, LPSTR szStatus, UINT nBufSize );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nBufSize_

> 用字符数指定缓冲区大小来检索字符串，包括终止空字符。你能指定 0，如果 _szStatus_ 为空。如果缓冲区大小不够， _szStatus_ 不会接收字符串。

_szStatus_

> 指定来接收字符串的缓冲区。如果指定值为空 (NULL)，会返回足够用来检索字符串的缓冲区大小。

## 返回值

> 用字符数返回缓冲区大小，足够用来检索包括终止空字符在内的字符串。
