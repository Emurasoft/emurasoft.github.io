# Editor\_GetWord

检索光标位置处的一个单词。你能直接用该内联函数或明确地发送 [EE\_GET\_WORD](../message/ee_get_word) 消息。

Editor\_GetWord( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nBufferSize_

用字符数指定复制到缓冲区的最大字符数，包括空字符。

_szBuffer_

指针指向会接收文本的缓冲区。

## 返回值

如果 _nBufferSize_ 是零，返回值是能接收文本的缓冲区的必需的大小字符数。如果 _nBufferSize_ 不是零，不使用返回值。

## 支持版本

支持 EmEditor 10.00 或之后的版本。
