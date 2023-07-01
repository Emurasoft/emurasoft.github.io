# Editor\_GetStatusW

检索显示在状态栏上的 Unicode 文本。你能直接用该内联函数或明确地发送 [EE\_GET\_STATUSW \
message](../message/ee_get_statusw).

Editor\_GetStatusW( HWND hwnd, LPWSTR szStatus, UINT nBufSize );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nBufSize_

> 用字符数指定缓冲区的大小，包括终止空字符。你能指定 0 如果 _szStatus_ 为空。如果缓冲区大小不够， _szStatus_ 不会检索任何字符串。

_szStatus_

> 指定要检索字符串的缓冲区。如果指定值为是空 (NULL)，返回足够的缓冲区大小来检索字符串。

## 返回值

> 返回 TRUE 如果当前标志允许或阻止在 EmEditor 中重新绘制变更。否则，返回 FALSE。
