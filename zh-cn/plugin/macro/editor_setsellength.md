# Editor\_SetSelLength

变更选区的字符长度。你能直接用该内联函数或明确地发送
[EE\_SET\_SEL\_LENGTH](../message/ee_set_sel_length)
消息。

Editor\_SetSelLength( HWND hwnd, UINT nLen );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nLen_

> 指定选区的字符长度。换行总是计为两个字符长度 (CR+LF)。

## 返回值

> 不使用返回值。