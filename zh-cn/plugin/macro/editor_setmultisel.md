# Editor\_SetMultiSel

当多个选取内容可用时，设置指定的选取内容的信息。你能直接用该内联函数或明确地发送 [EE\_SET\_MULTI\_SEL](../message/ee_set_multi_sel) 消息。

Editor\_SetMultiSel( HWND hwnd, UINT\_PTR iSel, const SEL\_INFO\* pSelInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_iSel_

> 将设置其信息的选取内容的索引。

_pSelInfo_

> 指针指向
> [SEL\_INFO](../structure/sel_info) 结构。

## 返回值

> 如果检索到指定的选取内容信息，则为 TRUE。如果选取内容不是多选模式或函数中发生错误，则返回值为 FALSE。