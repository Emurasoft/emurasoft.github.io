# EE_GET_TEXTW

检索文档文本。如果文档包含超过 `0x7ffffffe` 个 UTF-16 代码单元，则文本会被截断为该长度。你可以显式发送此消息，或使用 [Editor_GetTextW](../macro/editor_gettextw) 内联函数。

```
EE_GET_TEXTW
wParam = (WPARAM) (UINT) nBufferSize;
lParam = (LPARAM) (LPWSTR) szBuffer;
```

## 参数

_nBufferSize_

缓冲区的容量，以 `WCHAR` 元素为单位计算，并包含用于终止空字符（null）的空间。

_szBuffer_

指向接收文档文本的缓冲区的指针。

## 返回值

返回所需的缓冲区大小（以 `WCHAR` 元素为单位），包括终止空字符。

如果文档包含超过 `0x7ffffffe` 个 UTF-16 代码单元，则返回值为 `0x7fffffff`。如果发生错误，则返回 0。