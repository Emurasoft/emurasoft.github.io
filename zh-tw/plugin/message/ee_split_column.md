# EE\_SPLIT\_COLUMN

分割目前的 CSV 文檔的指定欄。你能明確地發送該消息或用 [Editor\_SplitColumn](../macro/editor_splitcolumn) 內嵌函式。

EE\_SPLIT\_COLUMN

wParam = (WPARAM)(SPLIT\_COLUMN\_INFO\*)pInfo;

lParam = 0;

## 參數

_pInfo_

指定指針指向 [SPLIT\_COLUMN\_INFO](../structure/split_column_info) 結構。

## 返回值

如果失敗，返回值為負。

## 版本

支持 EmEditor Professional 19.9 或之後的版本。
