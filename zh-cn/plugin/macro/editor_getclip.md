# Editor\_GetClip

在剪贴板记录中的指定位置处检索文本。你能直接用该内联函数或明确地发送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_GetClip( HWND hwnd, LPWSTR pszBuf, UINT cchBuf, UINT iPos, UINT\* pnFlags );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pszBuf_

指定接收文本的缓冲区。

_cchBuf_

用字符数指定缓冲区大小，包括终止空字符。

_iPos_

指定剪贴板记录中的位置。如果指定的（单位）是 -1，那么实际的剪贴板内容会被检索而不是剪贴板记录中的内容。

_nFlags_

这个值被实际的剪贴板格式填充。

|     |     |
| --- | --- |
| SEL\_TYPE\_CHAR | 剪贴板格式是标准文本。 |
| SEL\_TYPE\_LINE | 剪贴板格式是文本行。 |
| SEL\_TYPE\_BOX | 剪贴板格式是文本的垂直选区。 |

## 返回值

返回值是 pszBuf 缓冲区大小， 用包括终止空字符在内的需要接收文本的字符数表示。如果消息不成功，返回值是 -1。

## 支持版本

支持 EmEditor 9.00 或之后的版本。
