# EE\_GET\_SEL\_TYPE

获得选区状态的类型。你能明确地发送该消息或用 [Editor\_GetSelType](../macro/editor_getseltype) 内联函数或 [Editor\_GetSelTypeEx](../macro/editor_getseltypeex) 内联函数。

EE\_GET\_SEL\_TYPE

wParam = (WPARAM) (BOOL) bNeedAlways;

lParam = (LPARAM)0;

## 参数

_bNeedAlways_

> 如果参数是 TRUE，EE\_GET\_SEL\_TYPE 返回选区状态的类型，即使没有选取。如果参数是 FALSE, EE\_GET\_SEL\_TYPE 返回 SEL\_TYPE\_NONE 如果没有选取的话。

## 返回值

> 返回一个下列值的组合。SEL\_TYPE\_NONE，SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，和 SEL\_TYPE\_BOX 不能被组合。SEL\_TYPE\_KEYBOARD 和 SEL\_TYPE\_SELECTED 能与其他值组合。如果 bNeedAlways 是 TRUE，并且文本被选取的话，一个用 SEL\_TYPE\_SELECTED 的逻辑总数会被返回。如果 bNeedAlways 是 FALSE，不会使用 SEL\_TYPE\_SELECTED。
>
> | 值 | 含义 |
> | --- | --- |
> | SEL\_TYPE\_NONE | 没有选取。 |
> | SEL\_TYPE\_CHAR | 字符被选取。 |
> | SEL\_TYPE\_LINE | 行被选取。 |
> | SEL\_TYPE\_BOX | 框被选取。 |
> | SEL\_TYPE\_KEYBOARD | 用键盘选取。 |
> | SEL\_TYPE\_SELECTED | 已选取 (当 bNeedAlways = TRUE)。 |

## 支持版本

> 支持 EmEditor 3.00 或之后的版本。然而，bNeedAlways 支持 EmEditor 5.00 或之后的版本。在 5.00 之前的版本中，bNeedAlways 被假定为 FALSE。