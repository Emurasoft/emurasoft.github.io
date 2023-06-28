# EE\_GET\_STATUSW

检索显示在状态栏上的 Unicode 文本。你能明确地发送该消息或用 [Editor\_GetStatusW](../macro/editor_getstatusw) 内联函数。

EE\_GET\_STATUSW

wParam = nBufSize;

lParam = (LPARAM) (LPWSTR) szStatus;

## 参数

_nBufSize_

> 用字符数指定缓冲区的大小，包括终止空字符。你能指定 0 如果 _szStatus_ 为空。如果缓冲区大小不够， _szStatus_ 不会检索任何字符串。

_szStatus_

> 指定要检索字符串的缓冲区。如果指定值为是空 (NULL)，返回足够的缓冲区大小来检索字符串。

## 返回值

> 返回 TRUE 如果当前标志允许或阻止在 EmEditor 中重新绘制变更。否则，返回 FALSE。