# EE\_GET\_STATUSA

检索显示在状态栏上的 ANSI 文本。你能明确地发送该消息或用 [Editor\_GetStatusA 内联函数](../macro/editor_getstatusa)。

EE\_GET\_STATUSA

wParam = nBufLen;

lParam = (LPARAM) (LPSTR) szMessage;

## 参数

_nBufLen_

用字符数指定缓冲区的大小，包括终止空字符。你能指定 0 如果 _szMessage_ 为空。如果缓冲区大小不够， _szMessage_ 不会检索任何字符串。

_szMessage_

指定要检索字符串的缓冲区。如果指定的是空 (NULL)，返回足够的缓冲区大小来检索字符串。

## 返回值

返回 TRUE 如果当前标志允许或阻止在 EmEditor 中重新绘制变更。否则，返回 FALSE。
