# EE\_GET\_FILTER

檢索目前的文檔的篩選字串及設定。你能明確地發送該消息或用 [Editor\_GetFilter](../macro/editor_filter) 內嵌函式。

EE\_GET\_FILTER

wParam = (WPARAM) (FILTER\_INFO\_EX\*) pFilterInfo;

lParam = (LPARAM)(int)iFilter;

## 參數

_pFilterInfo_

> 指針指向 [FILTER\_INFO\_EX](../structure/filter_info_ex) 結構。

_iFilter_

> 指定你要檢索的字串及其設定的篩選器的索引，或指定 -1 來獲取篩選器的數目。

## 返回值

> 如果 iFilter 是 0 或更大的數字并且消息成功，返回值為 TRUE。如果 iFilter 是 -1，返回值是篩選器的數目。

## 版本

> 支持 EmEditor Professional Version 16.0 或之後的版本。
