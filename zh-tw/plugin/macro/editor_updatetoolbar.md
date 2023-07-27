# Editor\_UpdateToolbar

在工具列中更新一個按鈕的狀態。您能直接用該內嵌函式或明確地發送 [EE\_UPDATE\_TOOLBAR](../message/ee_update_toolbar) 消息。

Editor\_UpdateToolbar( HWND hwnd, UINT nCmdID );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nCmdID_

指定外掛程式的實例句柄。

## 返回值

不使用返回值。
