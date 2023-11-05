# EE\_GET\_MULTI\_SEL

當多個選區都可用時，檢索一個指定選區的信息。您能明確地發送該消息或用 [Editor\_GetMultiSel](../macro/editor_getmultisel) 內嵌函式。

```
EE_GET_MULTI_SEL
wParam = (WPARAM) (UINT_PTR) iSel;
lParam = (LPARAM) (SEL_INFO*) pSelInfo;
```

## 參數

_iSel_

要檢索信息的選區的索引。如果數值是 -1，那么選區的數目會被返回。

_pSelInfo_

指針指向
[SEL\_INFO](../../plugin/structure/sel_info) 結構。

## 返回值

如果 _iSel_ 是 -1，返回值是選區的數目。否則，返回值是 TRUE 如果指定選區的信息被檢索。返回值是 FALSE 如果選區不是多個選區或者函數發生錯誤。
