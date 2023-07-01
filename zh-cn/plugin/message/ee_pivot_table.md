# EE\_PIVOT\_TABLE

在 CSV 文档中创建数据透视表。你能明确地发送该消息或用 [Editor\_PivotTable](../macro/editor_pivottable) 内联函数。

EE\_PIVOT\_TABLE

wParam = (WPARAM)(PIVOT\_TABLE\_INFO\*)pInfo;

lParam = 0;

## 参数

_pInfo_

> 指定指向 [PIVOT\_TABLE\_INFO](../structure/pivot_table_info) 结构的指针。

## 返回值

> 如果失败，则返回值为负值。

## 支持版本

> 支持 EmEditor Professional 21.4 或之后的版本。
