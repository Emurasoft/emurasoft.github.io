# Editor\_LoadConfigA

重新載入由一個 ANSI 字串指定名稱的組態。您能直接用該內嵌函式或明確地發送 [EE\_LOAD\_CONFIGA](../message/ee_load_configa) 消息。

Editor\_LoadConfigA( HWND hwnd, LPCSTR szConfigName );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_szConfigName_

指定要重新載入的組態名稱。

## 返回值

不使用返回值。
