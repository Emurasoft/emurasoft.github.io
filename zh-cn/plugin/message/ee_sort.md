# EE\_SORT

排序文档。你可以明确地发送该消息或用 [Editor\_Sort](../macro/editor_sort) 内联函数。

EE\_SORT

wParam = 0;

lParam = (LPARAM) (SORT\_INFO\*) pSortInfo;

## 参数

_pSortInfo_

指向 [SORT\_INFO](../structure/sort_info) 结构。

## 返回值

返回 HRESULT 值。0 或正值表示成功，负值表示失败。

## 版本

支持 EmEditor Professional Version 16.4 或之后的版本。
