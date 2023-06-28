# EE\_SET\_OUTLINE\_ARRAY

为指定的多行设置大纲级别。你能明确地发送该消息或用
[Editor\_SetOutlineArray](../macro/editor_setoutlinearray) 内联函数。

EE\_SET\_OUTLINE\_ARRAY

wParam = (WPARAM) 0;

lParam = (LPARAM) (OUTLINE\_ARRAY\_INFO\*) pOutlineArrayInfo;

## 参数

_pOutlineArrayInfo_

> 指针指向一个 [OUTLINE\_ARRAY\_INFO](../structure/outline_array_info) 结构。

## 返回值

> 返回值是 FALSE 如果没有变更。否则，返回值是 TRUE。

## 支持版本

> 支持 EmEditor 13 或之后的版本。