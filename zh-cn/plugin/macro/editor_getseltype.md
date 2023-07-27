# Editor\_GetSelType

获得选区状态的类型。你能直接用该内联函数或明确地发送 [EE\_GET\_SEL\_TYPE](../message/ee_get_sel_type) 消息。

Editor\_GetSelType( HWND hwnd );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

## 返回值

返回一个下列值的组合。SEL\_TYPE\_NONE，SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，和 SEL\_TYPE\_BOX 不能被组合。只有 SEL\_TYPE\_KEYBOARD 能与其他值组合。

| 值 | 含义 |
| --- | --- |
| SEL\_TYPE\_NONE | 没有选取。 |
| SEL\_TYPE\_CHAR | 字符被选取。 |
| SEL\_TYPE\_LINE | 行被选取。 |
| SEL\_TYPE\_BOX | 框被选取。 |
| SEL\_TYPE\_KEYBOARD | 用键盘选取。 |

## 支持版本

支持 EmEditor 3.00 或之后的版本。
