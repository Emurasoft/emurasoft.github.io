# Editor\_GetStatusA

檢索顯示在狀態列上的 ANSI 文字。您能直接用該內嵌函式或明確地發送 [EE\_GET\_STATUSA 消息](../message/ee_get_statusa)。

Editor\_GetStatusA( HWND hwnd, LPSTR szStatus, UINT nBufSize );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nBufSize_

用字元數指定緩沖區大小來檢索字串，包括終止空字元。您能指定 0，如果 _szStatus_ 為空。如果緩沖區大小不夠， _szStatus_ 不會接收字串。

_szStatus_

指定來接收字串的緩沖區。如果指定值為空 (NULL)，會返回足夠用來檢索字串的緩沖區大小。

## 返回值

用字元數返回緩沖區大小，足夠用來檢索包括終止空字元在內的字串。
