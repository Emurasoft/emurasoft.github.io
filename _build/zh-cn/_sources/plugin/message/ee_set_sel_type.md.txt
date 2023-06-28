# EE\_SET\_SEL\_TYPE

设置选区状态的类型。你能明确地发送该消息或用 [Editor\_SetSelType](../macro/editor_setseltype) 内联函数或 [Editor\_SetSelTypeEx](../macro/editor_setseltypeex) 内联函数。

EE\_SET\_SEL\_TYPE

wParam = (WPARAM) (BOOL) bNeedAlways;

lParam = (LPARAM) nSelType;

## 参数

_bNeedAlways_

> 如果该参数是 TRUE，你能设置选区状态的类型即使没有选取任何文本。如果该参数是 FALSE，SEL\_TYPE\_NONE 将会取消对选择部分的选取。

_nSelType_

> 你能指定一个下列值的组合。然而，SEL\_TYPE\_NONE，SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，SEL\_TYPE\_BOX 不能联合使用。只有 SEL\_TYPE\_KEYBOARD 可以与 SEL\_TYPE\_NONE，
> SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，或 SEL\_TYPE\_BOX一起使用。
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_NONE | 没有选择。 |
> | SEL\_TYPE\_CHAR | 流选择模式。 |
> | SEL\_TYPE\_LINE | 行选择模式。 |
> | SEL\_TYPE\_BOX | 垂直选择模式。 |
> | SEL\_TYPE\_KEYBOARD | 指定键盘选择模式。这个值能与另一个值进行组合。 |

## 返回值

> 不使用。

## 支持版本

> 支持 EmEditor 3.00 或之后的版本。然而，bNeedAlways 支持 EmEditor 5.00 或之后的版本。在前几个版本中，bNeedAlways 被假定为 FALSE。