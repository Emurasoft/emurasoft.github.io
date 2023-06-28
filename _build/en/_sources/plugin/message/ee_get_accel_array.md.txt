# EE\_GET\_ACCEL\_ARRAY

檢索快捷鍵的數組。您能明確地發送該消息或用 [Editor\_GetAccelArray](../macro/editor_getaccelarray) 內嵌函式。

EE\_GET\_ACCEL\_ARRAY

wParam = (UINT) nBufSize;

lParam = (ACCEL\*) pAccel;

## 參數

_nBufSize_

> 在會檢索快捷鍵數列的 ACCEL 中，指定緩沖區的大小。

_pAccel_

> 指定指針指向檢索 ACCEL 結構數列的緩沖區。

## 返回值

> 返回值是在用來接收快捷鍵數列的 ACCEL 中的緩沖區大小。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。