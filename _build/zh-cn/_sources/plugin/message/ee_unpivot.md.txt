# EE\_UNPIVOT

通过平展 CSV 数据将列转换为行。你能明确地发送该消息或用 [Editor\_Unpivot](../macro/editor_unpivot) 内联函数。

EE\_UNPIVOT

wParam = (WPARAM)(UNPIVOT\*)pInfo;

lParam = 0;

## 参数

_pInfo_

> 指定指针指向 [UNPIVOT\_INFO](../structure/pivot_table_info) 结构。

## 返回值

> 如果失败，则返回值为负值。

## 支持版本

> 支持 EmEditor Professional 21.4 或之后的版本。