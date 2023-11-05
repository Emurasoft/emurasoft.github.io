# EE\_INFO\_EX

檢索或設定用於 EmEditor 的信息參數之一的值。你能明確地發送該消息或用 [Editor\_DocInfoEx](../macro/editor_docinfoex) 內嵌函式。

```
EE_INFO_EX
wParam = (WPARAM)(INFO_EX_DATA*)pInfo;
lParam = 0;
```

## 參數

_pInfo_

指針指向 [**INFO\_EX\_DATA** 結構](../structure/info_ex_data)。

## 返回值

取決於指定的參數。

## 支持版本

支持 EmEditor Professional v21.8 或之後的版本。
