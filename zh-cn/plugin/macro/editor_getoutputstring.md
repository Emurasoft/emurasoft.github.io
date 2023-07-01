# Editor\_GetOutputString

检索输出栏中的文本。你能直接用该内联函数或明确地发送 [EE\_GET\_OUTPUT\_STRING](../message/ee_get_output_string)
消息。

Editor\_GetOutputString( HWND hwnd, UINT cchBuf, LPWSTR pBuf );

## 参数

_cchBuf_

> 以字节为单位指定缓冲区大小，包括终止空字符。

_pBuf_

> 指定指针指向接收文本的缓冲区。

## 返回值

> 返回值是用来接收文本的以字节为单位的缓冲区大小，包括终止空字符。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。
