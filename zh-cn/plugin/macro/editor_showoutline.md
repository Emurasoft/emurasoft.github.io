# Editor\_ShowOutline

显示或隐藏大纲。你能直接用该内联函数或明确地发送 [EE\_SHOW\_OUTLINE](../message/ee_show_outline) 消息。

Editor\_ShowOutline( HWND hwnd, WPARAM nFlags );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nFlags_

指定下列值之一。

| 值 | 含义 |
| --- | --- |
| SHOW\_OUTLINE\_SHOW | 显示大纲。 |
| SHOW\_OUTLINE\_HIDE | 隐藏大纲。 |

## 返回值

不使用返回值。

## 版本

支持 EmEditor 6.00 或之后的版本。
