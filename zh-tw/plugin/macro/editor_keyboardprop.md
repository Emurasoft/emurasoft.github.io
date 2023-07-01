# Editor\_KeyboardProp

顯示指定命令 ID 和組態的鍵盤屬性。您能直接用該內嵌函式或明確地發送 [EE\_KEYBOARD\_PROP](../message/ee_keyboard_prop) 消息。

Editor\_KeyboardProp( HWND hwnd, UINT nCmdID, LPCWSTR pszConfigName );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nCmdID_

> 給鍵盤屬性上的初始選區指定命令 ID。

_pszConfigName_

> 指定 EmEditor 顯示鍵盤屬性的組態。

## 返回值

> 如果使用者在組態屬性上選擇 OK，返回值是 TRUE。如果使用者選擇 Cancel，返回值是 FALSE。
