# EE\_GET\_CELL

在指定单元格内检索 Unicode 文本。你能明确地发送这条消息或用 [Editor\_GetCell](../macro/editor_getcell) 内联函数。

EE\_GET\_CELL

wParam = (WPARAM) (GET\_CELL\_INFO\*) pGetCellInfo;

lParam = (LPARAM) (LPWSTR) szString;

## 参数

_pGetCellInfo_

> 指针指向 [GET\_CELL\_INFO](../structure/get_cell_info) 结构。

_szString_

> 指针指向要接收文本的缓冲区。

## 返回值

> 如果 _pGetCellInfo->cch_ 为零，返回值是一个缓冲区能接收文本的必需的大小，以字符为单位。如果 _pGetLineInfo->cch_ 不是零，则不使用返回值。如果 _pGetCellInfo->iColumn_ 是 -1，返回值是列数。