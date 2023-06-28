# Editor\_GetConfigA

檢索所選取的組態名稱為 ANSI 字串。您能直接用該內嵌函式或明確地發送 [EE\_GET\_CONFIGA](../message/ee_get_configa) 消息。

Editor\_GetConfigA( HWND hwnd, LPSTR szConfigName );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_szConfigName_

> 指定會接收組態名稱的一個緩沖區。緩沖區大小必須至少是 MAX\_CONFIG\_NAME 所標示的以位元為單位的值。

## 返回值

> 不使用返回值。