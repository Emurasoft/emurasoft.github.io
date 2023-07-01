# Editor\_ActivateTemp

把臨時文字作為一個新文檔打開。您能直接用該內嵌函式或明確地發送 [EE\_EDIT\_TEMP](../message/ee_edit_temp) 消息。

Editor\_ActivateTemp( HWND hwnd, UINT nEditID, POINT\_PTR\* pptInitialCaret = NULL );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nEditID_

> 指定您想要激活的臨時文字的 ID。S

_pptInitialCaret_

> 指定初始游標位置。

## 返回值

> 返回值是新文檔的 ID。

## 支持版本

> 支持 EmEditor 9.00 或之後的版本。
