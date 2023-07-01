# EE\_EXTRACT\_FREQUENT

將常用字串抽出到新文檔中。你可以明確地發送該消息或用 [Editor\_ExtractFrequent](../macro/editor_extractfrequent) 內嵌函式。

EE\_EXTRACT\_FREQUENT

wParam = (WPARAM) (EXTRACT\_FREQUENT\_INFO\*) pInfo;

lParam = 0;

## 參數s

_pInfo_

> 指針指向 [EXTRACT\_FREQUENT\_INFO 結構](../structure/extract_frequent_info)。

## 返回值

> 如果發生錯誤，則返回值為負。

## 版本

> 支持 EmEditor Professional Version 21.9 或之後的版本。
