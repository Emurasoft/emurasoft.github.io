# Editor\_GetMultiSel

當多個選區都可用時，檢索一個指定選區的信息。您能直接用該內嵌函式或明確地發送 [EE\_GET\_MULTI\_SEL](../message/ee_get_multi_sel) 消息。

Editor\_GetMultiSel( HWND hwnd, UINT\_PTR iSel, SEL\_INFO\* pSelInfo );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_iSel_

> 要檢索信息的選區的索引。如果數值是 -1，那么選區的數目會被返回。

_pSelInfo_

> 指標至
> [SEL\_INFO](../structure/sel_info) 結構。

## 返回值

> 如果 _iSel_ 是 -1，返回值是選區的數目。否則，返回值是 TRUE 如果指定選區的信息被檢索。返回值是 FALSE 如果選區不是多個選區或者函數發生錯誤。
