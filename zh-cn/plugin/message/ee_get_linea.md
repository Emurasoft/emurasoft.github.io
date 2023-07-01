# EE\_GET\_LINEA

在指定行检索 ANSI 文本。你能明确地发送该消息或用 [Editor\_GetLineA](../macro/editor_getlinea) 内联函数。

EE\_GET\_LINEA

wParam = (WPARAM) (GET\_LINE\_INFO\*) pGetLineInfo;

lParam = (LPARAM) (LPSTR) szString;

## 参数

_pGetLineInfo_

> 指定指针指向
> [GET\_LINE\_INFO](../structure/get_line_info)
> 结构。

_szString_

> 指针指向会接收文本的缓冲区。

## 返回值

> 如果 _pGetLineInfo->cch_ 为零，必须要有返回值字节数来表示接收文本的缓冲区。如果 _pGetLineInfo->cch_ 非零，不使用返回值。
