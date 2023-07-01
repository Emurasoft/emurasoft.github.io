# EE\_SET\_COLUMN

设置一列文本。你能明确地发送这条消息或用 [Editor\_SetColumn](../macro/editor_setcolumn) 内联函数。

EE\_SET\_COLUMN

wParam = (WPARAM) 0;

lParam = (LPARAM) (COLUMN\_STRUCT\*) pColumnStruct;

## 参数

_pColumnStruct_

> 指针指向 [COLUMN\_STRUCT](../structure/column_struct) 结构。

## 返回值

> 如果成功，返回值为零或正数值，如果失败，返回负数值。
