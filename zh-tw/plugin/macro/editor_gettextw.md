# Editor\_GetTextW

檢索文件文字。如果文件包含超過 `0x7ffffffe` 個 UTF-16 程式碼單元，文字會被截斷至該長度。你可以使用此內嵌函式，或是明確傳送 [EE\_GET\_TEXTW](../message/ee_get_textw) 訊息。

Editor\_GetTextW( HWND hwnd, UINT nBufferSize, LPWSTR szBuffer );

## 參數

_hwnd_

指定 EmEditor 的視圖或框架視窗控制代碼。

_nBufferSize_

緩衝區容量，以 `WCHAR` 元素為單位，包含結尾的空字元（null）所需空間。

_szBuffer_

指向接收文件文字之緩衝區的指標。

## 傳回值

傳回所需的緩衝區大小，以 `WCHAR` 元素為單位，包含結尾的空字元（null）。

如果文件包含超過 `0x7ffffffe` 個 UTF-16 程式碼單元，傳回值為 `0x7fffffff`。若發生錯誤則傳回 0。