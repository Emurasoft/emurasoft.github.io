# EE\_SET\_OUTLINE\_LEVEL

为指定的逻辑行设置大纲级别。你能明确地发送该消息或用 [Editor\_SetOutlineLevel](../macro/editor_setoutlinelevel) 内联函数。

EE\_SET\_OUTLINE\_LEVEL

wParam = (WPARAM) (INT\_PTR) nLogicalLine;

lParam = (LPARAM) (int) nLevel;

## 参数

_nLogicalLine_

> 指定一个逻辑行。

_nLevel_

> 指定一个大纲级别。

## 返回值

> 返回值是旧的指定逻辑行的大纲级别。如果发生错误，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。