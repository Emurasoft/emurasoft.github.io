# Editor\_GetAccelArray

检索快捷键的数组。你能直接用该内联函数或明确地发送 [EE\_GET\_ACCEL\_ARRAY](../message/ee_get_accel_array) 消息。

Editor\_GetAccelArray( HWND hwnd, ACCEL\* pAccel, UINT nBufSize );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nBufSize_

> 在会检索快捷键数列的 ACCEL 中，指定缓冲区的大小。

_pAccel_

> 指定指针指向检索 ACCEL 结构数列的缓冲区。

## 返回值

> 返回值是在用来接收快捷键数列的 ACCEL 中的缓冲区大小。

## 支持版本

> 支持 EmEditor 7.00 或之后的版本。
