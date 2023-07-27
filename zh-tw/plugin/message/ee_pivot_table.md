# EE\_PIVOT\_TABLE

在 CSV 文檔中建立樞紐分析表。你能明確地發送該消息或用 [Editor\_PivotTable](../macro/editor_pivottable) 內嵌函式。

EE\_PIVOT\_TABLE

wParam = (WPARAM)(PIVOT\_TABLE\_INFO\*)pInfo;

lParam = 0;

## 參數

_pInfo_

指定指向 [PIVOT\_TABLE\_INFO](../structure/pivot_table_info) 結構的指針。

## 返回值

如果失敗，則返回值為負值。

## 支持版本

支持 EmEditor Professional 21.4 或之後的版本。
