# EE\_GET\_ACCEL\_ARRAY

检索快捷键的数组。你能明确地发送该消息或用 [Editor\_GetAccelArray](../macro/editor_getaccelarray) 内联函数。

```
EE_GET_ACCEL_ARRAY
wParam = (UINT) nBufSize;
lParam = (ACCEL*) pAccel;
```

## 参数

_nBufSize_

在会检索快捷键数列的 ACCEL 中，指定缓冲区的大小。

_pAccel_

指定指针指向检索 ACCEL 结构数列的缓冲区。

## 返回值

返回值是在用来接收快捷键数列的 ACCEL 中的缓冲区大小。

## 支持版本

支持 EmEditor 7.00 或之后的版本。
