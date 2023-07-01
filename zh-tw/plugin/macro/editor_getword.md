# Editor\_GetWord

檢索游標位置處的一個單字。您能直接用該內嵌函式或明確地發送 [EE\_GET\_WORD](../message/ee_get_word) 消息。

Editor\_GetWord( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nBufferSize_

> 用字元數指定複製到緩沖區的最大字元數，包括空字元。

_szBuffer_

> 指標至會接收文字的緩沖區。

## 返回值

> 如果 _nBufferSize_ 是零，返回值是能接收文字的緩沖區的必需的大小字元數。如果 _nBufferSize_ 不是零，不使用返回值。

## 支持版本

> 支持 EmEditor 10.00 或之後的版本。
