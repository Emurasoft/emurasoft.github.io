# Editor\_GetSelTextA

检索被选取的 ANSI 文本。你能直接用该内联函数或明确地发送 [EE\_GET\_SEL\_TEXTA](../message/ee_get_sel_texta) 消息。

Editor\_GetSelTextA( HWND hwnd, UINT nBufferSize, LPSTR szBuffer );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nBufferSize_

> 以字节为单位指定最大的字符数来复制到缓冲区，包括空字符。

_szBuffer_

> 指针指向会接收文本的缓冲区。

## 返回值

> 如果 _nBufferSize_ 为零，那么以字节为单位的返回值是一个会接收文本的缓冲区的必需大小。如果 _nBufferSize_ 为非零，不使用返回值。