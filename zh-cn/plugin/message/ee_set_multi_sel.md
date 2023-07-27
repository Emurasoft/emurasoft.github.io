# EE\_SET\_MULTI\_SEL

当多个选取内容可用时，设置指定的选取内容的信息。你能明确地发送该消息或用
[Editor\_SetMultiSel](../macro/editor_setmultisel) 内联函数。

EE\_SET\_MULTI\_SEL

wParam = (WPARAM) (UINT\_PTR) iSel;

lParam = (LPARAM) (const SEL\_INFO\*) pSelInfo;

## 参数

_iSel_

将设置其信息的选取内容的索引。

_pSelInfo_

指针指向
[SEL\_INFO](../structure/sel_info) 结构。

## 返回值

如果检索到指定的选取内容信息，则为 TRUE。如果选取内容不是多选模式或函数中发生错误，则返回值为 FALSE。
