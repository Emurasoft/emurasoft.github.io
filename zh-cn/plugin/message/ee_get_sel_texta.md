# EE\_GET\_SEL\_TEXTA

检索被选取的 ANSI 文本。你能明确地发送该消息或用 [Editor\_GetSelTextA](../macro/editor_getseltexta) 内联函数。

EE\_GET\_SEL\_TEXTA

wParam = (WPARAM) (UINT) nBufferSize;

lParam = (LPARAM) (LPSTR) szBuffer;

## 参数

_nBufferSize_

> 用字节数指定最大的字符数来复制到缓冲区，包括空字符。

_szBuffer_

> 指针指向会接收文本的缓冲区。

## 返回值

> 如果 _nBufferSize_ 为零，那返回值是用字节数表示的一个会接收文本的缓冲区的必需大小。如果 _nBufferSize_ 为非零，不使用返回值。