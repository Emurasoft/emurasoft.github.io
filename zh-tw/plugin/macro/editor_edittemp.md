# Editor\_EditTemp

把臨時文字作為一個新文檔打開。您能直接用該內嵌函式或明確地發送 [EE\_EDIT\_TEMP](../message/ee_edit_temp)
消息。

Editor\_EditTemp( HWND hwnd, LPCWSTR pszTempText, LPCWSTR pszTitle, LPCWSTR pszIconPath, LPCWSTR pszConfig, UINT nEncoding, POINT\_PTR\* pptInitialCaret = NULL, UINT nFlags = 0 );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pszTempText_

指定您想要作為一個新文檔打開的內存上的臨時文字。

_pszTitle_

指定新文檔的標題。

_pszIconPath_

指定您想要用作新文檔的圖示的路徑和檔案名稱。

_pszConfig_

指定新文檔應使用的組態名稱。

_nEncoding_

指定檔案的編碼。

_pptInitialCaret_

指定初始游標位置。

_nFlags_

這個值必須是 0。

## 返回值

返回值是新文檔的 ID。

## 支持版本

支持 EmEditor 9.00 或之後的版本。
