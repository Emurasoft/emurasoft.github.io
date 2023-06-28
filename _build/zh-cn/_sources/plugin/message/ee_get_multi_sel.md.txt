# EE\_GET\_MULTI\_SEL

当多个选区都可用时，检索一个指定选区的信息。你能明确地发送该消息或用 [Editor\_GetMultiSel](../macro/editor_getmultisel) 内联函数。

EE\_GET\_MULTI\_SEL

wParam = (WPARAM) (UINT\_PTR) iSel;

lParam = (LPARAM) (SEL\_INFO\*) pSelInfo;

## 参数

_iSel_

> 要检索信息的选区的索引。如果数值是 -1，那么选区的数目会被返回。

_pSelInfo_

> 指针指向
> [SEL\_INFO](../../plugin/structure/sel_info) 结构。

## 返回值

> 如果 _iSel_ 是 -1，返回值是选区的数目。否则，返回值是 TRUE 如果指定选区的信息被检索。返回值是 FALSE 如果选区不是多个选区或者函数发生错误。