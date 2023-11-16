# Editor\_GetStatusW

檢索顯示在狀態列上的 Unicode 文字。您能直接用該內嵌函式或明確地發送 [EE\_GET\_STATUSW message](../message/ee_get_statusw).

Editor\_GetStatusW( HWND hwnd, LPWSTR szStatus, UINT nBufSize );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nBufSize_

用字元數指定緩沖區的大小，包括終止空字元。您能指定 0 如果 _szStatus_ 為空。如果緩沖區大小不夠， _szStatus_ 不會檢索任何字串。

_szStatus_

指定要檢索字串的緩沖區。如果指定值為是空 (NULL)，返回足夠的緩沖區大小來檢索字串。

## 返回值

返回 TRUE 如果目前的標志允許或阻止在 EmEditor 中重新繪制變更。否則，返回 FALSE。
