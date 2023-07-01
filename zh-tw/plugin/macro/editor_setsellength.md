# Editor\_SetSelLength

變更選區的字元長度。您能直接用該內嵌函式或明確地發送
[EE\_SET\_SEL\_LENGTH](../message/ee_set_sel_length)
消息。

Editor\_SetSelLength( HWND hwnd, UINT nLen );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nLen_

> 指定選區的字元長度。換行總是計為兩個字元長度 (CR+LF)。

## 返回值

> 不使用返回值。
