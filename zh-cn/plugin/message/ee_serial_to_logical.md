# EE\_SERIAL\_TO\_LOGICAL

把序列位置转换为逻辑坐标。序列位置是以零为初始值的整个文本起始处的字符的索引。
你能明确地发送该消息或用
[Editor\_SerialToLogical](../macro/editor_serialtological)
内联函数。

EE\_SERIAL\_TO\_LOGICAL

wParam = (WPARAM) (UINT) nSerial;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical;

## 参数

_nSerial_

> 指定一个要被转换的序列位置。

_pptLogical_

> 指针指向一个将接收转换后的逻辑坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

> 返回序列位置。
