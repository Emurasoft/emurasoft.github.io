# Editor\_GetLineA

在指定行检索 ANSI 文本。你能直接用该内联函数或明确地发送 [EE\_GET\_LINEA](../message/ee_get_linea) 消息。

Editor\_GetLineA( HWND hwnd, GET\_LINE\_INFO\* pGetLineInfo, LPSTR szString );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pGetLineInfo_

> 指针指向 [GET\_LINE\_INFO](../structure/get_line_info) 结构。

_szString_

> 指针指向会接收文本的缓冲区。

## 返回值

> 如果 _pGetLineInfo->cch_  为零，必须要有以字节为单位的返回值来表示接收文本的缓冲区。如果 _pGetLineInfo->cch_ 非零，不使用返回值。
