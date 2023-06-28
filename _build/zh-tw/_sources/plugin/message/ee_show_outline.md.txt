# EE\_SHOW\_OUTLINE

顯示或隱藏大綱。您能明確地發送該消息或用 [Editor\_ShowOutline](../macro/editor_showoutline) 內嵌函式。

EE\_SHOW\_OUTLINE

wParam = (WPARAM) (INT\_PTR) nFlags;

lParam = 0;

## 參數

_nFlags_

> 指定下列值之一。
>
> | 值 | 含義 |
> | --- | --- |
> | SHOW\_OUTLINE\_SHOW | 顯示大綱。 |
> | SHOW\_OUTLINE\_HIDE | 隱藏大綱。 |

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。