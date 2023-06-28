# EE\_SET\_MULTI\_SEL

當多個選取內容可用時，設定指定的選取內容的信息。你能明確地發送該消息或用
[Editor\_SetMultiSel](../macro/editor_setmultisel) 內嵌函式。

EE\_SET\_MULTI\_SEL

wParam = (WPARAM) (UINT\_PTR) iSel;

lParam = (LPARAM) (const SEL\_INFO\*) pSelInfo;

## 參數

_iSel_

> 將設定其信息的選取內容的索引。

_pSelInfo_

> 指針指向
> [SEL\_INFO](../structure/sel_info) 結構。

## 返回值

> 如果檢索到指定的選取內容信息，則為 TRUE。如果選取內容不是多選模式或函數中發生錯誤，則返回值為 FALSE。