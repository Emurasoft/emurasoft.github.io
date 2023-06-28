# EE\_FILTER

用指定字符串和设定筛选文档。你能明确地发送这条消息或用 [Editor\_Filter](../macro/editor_filter) 内联函数。

EE\_FILTER

wParam = (WPARAM) (FILTER\_INFO\*) pFilterInfo;

lParam = 0;

## 参数

_pFilterInfo_

> 指针指向 [FILTER\_INFO](../structure/filter_info) 结构。

## 返回值

> 返回值是与指定字符串相匹配的行数。如果指定字符串是一个空字符串，那么返回值是 -1。如果指定的是 FLAG\_FIND\_CONTINUE，那返回值是 0。