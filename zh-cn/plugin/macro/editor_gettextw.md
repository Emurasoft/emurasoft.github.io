# Editor_GetTextW

检索文档文本。如果文档包含超过 `0x7ffffffe` 个 UTF-16 代码单元，则文本会被截断为该长度。你可以使用此内联函数，或显式发送 [EE_GET_TEXTW](../message/ee_get_textw) 消息。

Editor_GetTextW( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## 参数

_hwnd_

指定 EmEditor 的视图或框架窗口句柄。

_nBufferSize_

缓冲区容量（以 `WCHAR` 元素计），包括用于终止空字符的空间。

_szBuffer_

指向接收文档文本的缓冲区的指针。

## 返回值

返回所需的缓冲区大小（以 `WCHAR` 元素计），包括终止空字符。

如果文档包含超过 `0x7ffffffe` 个 UTF-16 代码单元，则返回值为 `0x7fffffff`。如果发生错误，则返回 0。