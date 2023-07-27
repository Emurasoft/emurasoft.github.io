# Editor\_SaveTemp

儲存臨時文字。您能直接用該內嵌函式或明確地發送 [EE\_EDIT\_TEMP](../message/ee_edit_temp)
消息。

Editor\_SaveTemp( HWND hwnd, UINT nEditID );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nEditID_

指定您想要保持的臨時文字的 ID。

## 返回值

返回值是新文檔的 ID。

## 支持版本

支持 EmEditor 9.00 或之後的版本。
