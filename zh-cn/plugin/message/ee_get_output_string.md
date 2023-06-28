# EE\_GET\_OUTPUT\_STRING

检索输出栏中的文本。你能明确地发送该消息或用 [Editor\_GetOutputString](../macro/editor_getoutputstring) 内联函数。

EE\_GET\_OUTPUT\_STRING

wParam = (WPARAM) (UINT) cchBuf;

lParam = (LPARAM) (LPWSTR) pBuf;

## 参数

_cchBuf_

> 用字节数指定缓冲区大小，包括终止空字符。

_pBuf_

> 指定指针指向接收文本的缓冲区。

## 返回值

> 返回值是用来接收文本的缓冲区大小字节数，包括终止空字符。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。