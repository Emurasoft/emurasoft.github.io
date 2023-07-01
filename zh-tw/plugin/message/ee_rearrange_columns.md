# EE\_REARRANGE\_COLUMNS

重排 CSV 欄。你能明確地發送該消息或用 [Editor\_RearrangeColumns](../macro/editor_rearrangecolumns) 內嵌函式。

EE\_REARRANGE\_COLUMNS

wParam = (WPARAM) (REARRANGE\_COLULMNS\_INFO\*)pInfo;

lParam = 0;

## 參數

_pInfo_

> 指定指針指向 [REARRANGE\_COLUMNS\_INFO](../structure/rearrange_columns_info) 結構。

## 返回值

> 如果消息成功，則返回值為零。如果消息失敗，則返回值非零。

## 版本

> 支持 EmEditor Professional v22.1 或之後的版本。
