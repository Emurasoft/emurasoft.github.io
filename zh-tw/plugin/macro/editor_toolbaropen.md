# Editor\_ToolbarOpen

打開自訂工具列。您能直接用該內嵌函式或明確地發送 [EE\_TOOLBAR\_OPEN](../message/ee_toolbar_open)
消息。

Editor\_ToolbarOpen( HWND hwnd, TOOLBAR\_INFO\* pToolbarInfo );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pToolbarInfo_

指標至 TOOLBAR\_INFO 結構。

## 返回值

返回值是一個自訂工具列 ID。如果消息失敗，返回值為零。

## 支持版本

支持 EmEditor 7.00 或之後的版本。
