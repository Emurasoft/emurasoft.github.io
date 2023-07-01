# Editor\_GetCell

在指定的单元格内检索 Unicode 文本。你能用该内联函数或明确地发送
[EE\_GET\_CELL](../message/ee_get_cell) 消息。

Editor\_GetCell( HWND hwnd, GET\_CELL\_INFO\* pGetCellInfo, LPWSTR szString );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pGetCellInfo_

> 指针指向 [GET\_CELL\_INFO](../structure/get_cell_info) 结构。

_szString_

> 指针指向要接收文本的缓冲区。

## 返回值

> 如果 _pGetCellInfo->cch_ 是零，返回值是一个缓冲区能接收文本的必需的大小，以字符为单位。如果 _pGetLineInfo->cch_ 不是零，则不使用返回值。如果 _pGetCellInfo->iColumn_ 是 -1，返回值,是列数。
