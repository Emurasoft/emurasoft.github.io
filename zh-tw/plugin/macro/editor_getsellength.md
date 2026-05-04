# Editor_GetSelLength

檢索所選取文字的長度。您可以使用此內嵌函式，或明確傳送 [EE_GET_SEL_LENGTH](../message/ee_get_sel_length) 訊息。

nLen = Editor_GetSelLength( HWND hwnd, size_t nMaxLen = 0 );

## 參數

_hwnd_

指定 EmEditor 的視窗（檢視或框架）的視窗控制代碼。

_nMaxLen_

指定最大長度。如果長度超過此值，則返回該值。

## 返回值

返回值為所選取文字的長度。

## 版本

支持 EmEditor Professional 26.1 或更新版本。