# Editor\_SetMultiSel

當多個選取內容可用時，設定指定的選取內容的信息。你能直接用該內嵌函式或明確地發送 [EE\_SET\_MULTI\_SEL](../message/ee_set_multi_sel) 消息。

Editor\_SetMultiSel( HWND hwnd, UINT\_PTR iSel, const SEL\_INFO\* pSelInfo );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控點。

_iSel_

> 將設定其信息的選取內容的索引。

_pSelInfo_

> 指針指向
> [SEL\_INFO](../structure/sel_info) 結構。

## 返回值

> 如果檢索到指定的選取內容信息，則為 TRUE。如果選取內容不是多選模式或函數中發生錯誤，則返回值為 FALSE。
