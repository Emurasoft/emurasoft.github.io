# EE\_SORT

排序文檔。你可以明確地發送該消息或用 [Editor\_Sort](../macro/editor_sort) 內嵌函式。

EE\_SORT

wParam = 0;

lParam = (LPARAM) (SORT\_INFO\*) pSortInfo;

## 參數

_pSortInfo_

指向 [SORT\_INFO](../structure/sort_info) 結構。

## 返回值

返回 HRESULT 值。0 或正值表示成功，負值表示失敗。

## 版本

支持 EmEditor Professional Version 16.4 或之後的版本。
