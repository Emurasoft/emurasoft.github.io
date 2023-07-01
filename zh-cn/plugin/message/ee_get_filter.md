# EE\_GET\_FILTER

检索当前文档的筛选字符串及设定。你能明确地发送该消息或用 [Editor\_GetFilter](../macro/editor_filter) 内联函数。

EE\_GET\_FILTER

wParam = (WPARAM) (FILTER\_INFO\_EX\*) pFilterInfo;

lParam = (LPARAM)(int)iFilter;

## 参数

_pFilterInfo_

> 指针指向 [FILTER\_INFO\_EX](../structure/filter_info_ex) 结构。

_iFilter_

> 指定你要检索的字符串及其设定的筛选器的索引，或指定 -1 来获取筛选器的数目。

## 返回值

> 如果 iFilter 是 0 或更大的数字并且消息成功，返回值为 TRUE。如果 iFilter 是 -1，返回值是筛选器的数目。

## 版本

> 支持 EmEditor Professional Version 16.0 或之后的版本。
