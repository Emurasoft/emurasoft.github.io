# EE\_GET\_OUTLINE\_LEVEL

检索指定逻辑行的大纲级别。你能明确地发送该消息或用 [Editor\_GetOutlineLevel](../macro/editor_getoutlinelevel) 内联函数。

EE\_GET\_OUTLINE\_LEVEL

wParam = (WPARAM) (INT\_PTR) nLogicalLine;

lParam = 0;

## 参数

_nLogicalLine_

> 指定一个逻辑行。

## 返回值

> 返回值是指定逻辑行的大纲级别。如果发生错误，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。
