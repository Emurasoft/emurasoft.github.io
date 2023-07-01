# Editor\_GetAccelArray

檢索快速鍵的數組。您能直接用該內嵌函式或明確地發送 [EE\_GET\_ACCEL\_ARRAY](../message/ee_get_accel_array) 消息。

Editor\_GetAccelArray( HWND hwnd, ACCEL\* pAccel, UINT nBufSize );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nBufSize_

> 在會檢索快速鍵數列的 ACCEL 中，指定緩沖區的大小。

_pAccel_

> 指定指標至檢索 ACCEL 結構數列的緩沖區。

## 返回值

> 返回值是在用來接收快速鍵數列的 ACCEL 中的緩沖區大小。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。
