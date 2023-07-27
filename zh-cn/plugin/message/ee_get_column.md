# EE\_GET\_COLUMN

在 CSV 模式中检索一列文本。你能明确地发送这条消息或用 [Editor\_GetColumn](../macro/editor_getcolumn) 内联函数。

EE\_GET\_COLUMN

wParam = (WPARAM) 0;

lParam = (LPARAM) (COLUMN\_STRUCT\*) pColumnStruct;

## 参数

_pColumnStruct_

指针指向 [COLUMN\_STRUCT](../structure/column_struct) 结构。

## 返回值

返回值是缓冲区的大小，包括如果成功检索文本所需的终止 NULL 的字符数，或者如果失败的负值。返回值可以大于检索文本的确切大小。
