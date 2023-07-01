# Editor\_GetSelTextW

檢索被選取的 Unicode 文字。您能直接用該內嵌函式或明確地發送 [EE\_GET\_SEL\_TEXTW](../message/ee_get_sel_textw) 消息。

Editor\_GetSelTextW( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nBufferSize_

> 用單字數指定最大字元數來複製到緩沖區，包括空字元。

_szBuffer_

> 指標至會接收文字的緩沖區。

## 返回值

> 如果 _nBufferSize_ 為零，那以位元為單位的返回值是一個會接收文字的緩沖區的必需大小。如果 _nBufferSize_ 為非零，不使用返回值。
