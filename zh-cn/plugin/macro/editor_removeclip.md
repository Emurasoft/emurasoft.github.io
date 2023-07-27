# Editor\_RemoveClip

在剪贴板记录上的指定位置处删除文本。你能直接用该内联函数或明确地发送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_RemoveClip( HWND hwnd, UINT iPos, UINT nFlags );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_iPos_

指定剪贴板记录上的位置。

_nFlags_

指定要删除的剪贴板的格式。

|     |     |
| --- | --- |
| SEL\_TYPE\_CHAR | 剪贴板格式是标准文本。 |
| SEL\_TYPE\_LINE | 剪贴板格式是文本行。 |
| SEL\_TYPE\_BOX | 剪贴板格式是文本的垂直选区。 |

## 返回值

返回值是剪贴板记录上文本被删除的位置。如果消息没有成功，返回值是 -1。

## 支持版本

支持 EmEditor 9.00 或之后的版本。
