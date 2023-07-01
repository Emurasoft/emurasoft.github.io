# Editor\_SetSelTypeEx

设置选区状态的类型。你能直接用该内联函数或明确地发送
the [EE\_SET\_SEL\_TYPE message](../message/ee_set_sel_type).

Editor\_SetSelTypeEx( hwnd, bNeedAlways, nSelType );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_bNeedAlways_

> 如果该参数是 TRUE，你能设置选区状态的类型即使没有选取任何文本。如果该参数是 FALSE，SEL\_TYPE\_NONE 将会取消对选择部分的选取。

_nSelType_

> 你能指定一个下列值的组合。 However,
> SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, SEL\_TYPE\_BOX cannot be
> combined. Only SEL\_TYPE\_KEYBOARD can be combined with SEL\_TYPE\_NONE,
> SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, or SEL\_TYPE\_BOX.
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

> 支持 EmEditor 5.00 或之后的版本。
