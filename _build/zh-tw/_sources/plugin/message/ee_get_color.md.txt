# EE\_GET\_COLOR

檢索指定部分的文本、背景顏色以及樣式。您能明確地送出該信息或用 [Editor\_GetColor](../macro/editor_getcolor) 內嵌函式。

EE\_GET\_COLOR

wParam = 0;

lParam = (LPARAM) (GET\_COLOR\_INFO\*) pGetColorInfo;

## 參數

_pGetColorInfo_

> 指針指向 [GET\_COLOR\_INFO](../structure/get_color_info) 結構。

## 返回值

> 返回值是 TRUE 如果通過的話，或 FALSE 如果未通過的話。

## 支持版本

> 支持 Version 14.4 以及之後的版本。