# Editor\_EditTemp

把臨時文字作為一個新文檔打開。您能直接用該內嵌函式或明確地發送 [EE\_EDIT\_TEMP](../message/ee_edit_temp)
消息。

Editor\_EditTemp( HWND hwnd, LPCWSTR pszTempText, LPCWSTR pszTitle, LPCWSTR pszIconPath, LPCWSTR pszConfig, UINT nEncoding, const POINT\_PTR\* pptInitialCaret = NULL, UINT nFlags = 0 );

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

指定以下值之一。

|     |     |
| --- | --- |
| TEMP\_INFO\_OPEN | 打開一個臨時文字檔案。 |
| TEMP\_INFO\_NO\_ID | 打開一個臨時文字檔案，不設定 ID。使用此旗標打開的文檔可以在使用者選擇 **「檔案」** 功能表中的 **「另存新檔」** 時儲存到檔案中。 |

## 返回值

返回值是新文檔的 ID。

## 支持版本

支持 EmEditor 9.00 或之後的版本。
