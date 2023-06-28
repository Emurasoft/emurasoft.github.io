# EE\_COMPARE

比較兩個檔案。你能明確地發送該消息或用 [Editor\_Compare](../macro/editor_compare) 內嵌函式。

EE\_COMPARE

wParam = (WPARAM) (COMPARE\_INFO\*) pCompareInfo;

lParam = 0;

## 參數

_pCompareInfo_

> 指針指向 [COMPARE\_INFO](../structure/compare_info) 結構。

## 返回值

> 返回值可以是以下值之一。 如果發生錯誤，返回值為負值。
>
> |     |     |
> | --- | --- |
> | E\_DOCUMENT\_1\_NOT\_FOUND | 找不到第一個檔案。 |
> | E\_DOCUMENT\_2\_NOT\_FOUND | 找不到第二個檔案。 |
> | E\_FAIL | 未指定的錯誤。 |
> | E\_NOT\_MDI | 必須啟用 Tab。 |
> | S\_DIFF | 兩個文檔不相同。 |
> | S\_MATCHED | 兩個文檔相同。 |
> | S\_MATCHED\_IGNORED | 除了被忽略的地方外，兩個文檔是相同的。 |

## 支持版本

> 支持 EmEditor Professional v17.7 或之後的版本。