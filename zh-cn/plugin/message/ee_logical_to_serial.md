# EE\_LOGICAL\_TO\_SERIAL

把逻辑坐标转换为序列位置。序列位置是以零为初始值的整个文本起始处的字符的索引。
你能明确地发送该消息或用
[Editor\_LogicalToSerial](../macro/editor_logicaltoserial)
内联函数。

EE\_LOGICAL\_TO\_SERIAL

wParam = 0;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical

## 参数

_pptLogical_

指针指向一个指定要被转换的逻辑坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

返回序列位置。
