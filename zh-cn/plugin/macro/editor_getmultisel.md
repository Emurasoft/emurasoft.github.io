# Editor\_GetMultiSel

当多个选区都可用时，检索一个指定选区的信息。你能直接用该内联函数或明确地发送 [EE\_GET\_MULTI\_SEL](../message/ee_get_multi_sel) 消息。

Editor\_GetMultiSel( HWND hwnd, UINT\_PTR iSel, SEL\_INFO\* pSelInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_iSel_

> 要检索信息的选区的索引。如果数值是 -1，那么选区的数目会被返回。

_pSelInfo_

> 指针指向
> [SEL\_INFO](../structure/sel_info) 结构。

## 返回值

> 如果 _iSel_ 是 -1，返回值是选区的数目。否则，返回值是 TRUE 如果指定选区的信息被检索。返回值是 FALSE 如果选区不是多个选区或者函数发生错误。