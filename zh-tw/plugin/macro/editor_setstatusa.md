# Editor\_SetStatusA

在狀態列上顯示一條 ANSI 消息。您能直接用該內嵌函式或明確地發送 [EE\_SET\_STATUSA](../message/ee_set_statusa) 消息。

Editor\_SetStatusA( HWND hwnd, LPCSTR szStatus );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_szStatus_

指定要顯示在狀態列上的消息文字。

## 返回值

不使用返回值。
