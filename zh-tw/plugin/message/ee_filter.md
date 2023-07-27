# EE\_FILTER

用指定字串和設定篩選文檔。您能明確地發送這條消息或用 [Editor\_Filter](../macro/editor_filter) 內嵌函式。

EE\_FILTER

wParam = (WPARAM) (FILTER\_INFO\*) pFilterInfo;

lParam = 0;

## 參數

_pFilterInfo_

指針指向 [FILTER\_INFO](../structure/filter_info) 結構。

## 返回值

返回值是與指定字串相符合的行數。如果指定字串是一個空字串，那么返回值是 -1。如果指定的是 FLAG\_FIND\_CONTINUE，那返回值是 0。
