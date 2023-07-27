# EE\_GET\_COLOR

检索指定部分的文本、背景颜色以及样式。你能明确地送出该信息或用 [Editor\_GetColor](../macro/editor_getcolor) 内联函数。

EE\_GET\_COLOR

wParam = 0;

lParam = (LPARAM) (GET\_COLOR\_INFO\*) pGetColorInfo;

## 参数

_pGetColorInfo_

指针指向 [GET\_COLOR\_INFO](../structure/get_color_info) 结构。

## 返回值

返回值是 TRUE 如果通过的话，或 FALSE 如果未通过的话。

## 支持版本

支持 Version 14.4 以及之后的版本。
