# EE\_GET\_WORD

检索光标位置处的一个单词。你能明确地发送该消息或用 [Editor\_GetWord](../macro/editor_getword) 内联函数。

EE\_GET\_WORD

wParam = (WPARAM) (UINT) nBufferSize;

lParam = (LPARAM) (LPWSTR) szBuffer;

## 参数

_nBufferSize_

> 用字符数指定复制到缓冲区的最大字符数，包括空字符。

_szBuffer_

> 指针指向会接收文本的缓冲区。

## 返回值

> 如果 _nBufferSize_ 是零，返回值是用字符数表示的一个会接收文本的缓冲区的必需大小。如果 _nBufferSize_ 不是零，不使用返回值。

## 支持版本

> 支持 EmEditor 10.00 或之后的版本。
