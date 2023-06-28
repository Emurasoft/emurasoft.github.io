# EE\_SHOW\_OUTLINE

显示或隐藏大纲。你能明确地发送该消息或用 [Editor\_ShowOutline](../macro/editor_showoutline) 内联函数。

EE\_SHOW\_OUTLINE

wParam = (WPARAM) (INT\_PTR) nFlags;

lParam = 0;

## 参数

_nFlags_

> 指定下列值之一。
>
> | 值 | 含义 |
> | --- | --- |
> | SHOW\_OUTLINE\_SHOW | 显示大纲。 |
> | SHOW\_OUTLINE\_HIDE | 隐藏大纲。 |

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。