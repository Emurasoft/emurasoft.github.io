# Editor\_GetMargin

检索边距大小。你能直接用该内联函数或明确地发送 [EE\_GET\_MARGIN](../message/ee_get_margin)
消息。

Editor\_Convert( HWND hwnd );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

## 返回值

返回当前被选取的边距大小。如果标准行边距大小以及引用行边距大小不同，更大的边距值会被返回。如果换行方式是按窗口大小换行，返回值取决于当前窗口大小。
