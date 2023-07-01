# Editor\_InsertClip

在剪贴板记录上的指定位置处插入文本。你能直接用该内联函数或明确地发送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_InsertClip( HWND hwnd, LPCWSTR pszText, UINT iPos, UINT nFlags );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pszText_

> 指定要插入的文本。

_iPos_

> 在剪贴板记录上指定旧的位置。

_nFlags_

> 指定要插入或删除的剪贴板的格式。
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 剪贴板格式是标准文本。 |
> | SEL\_TYPE\_LINE | 剪贴板格式是文本行。 |
> | SEL\_TYPE\_BOX | 剪贴板格式是文本的垂直选区。 |

## 返回值

> 返回值是剪贴板记录上的新文本被插入的位置处。如果消息失败，返回值是　－１。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。
