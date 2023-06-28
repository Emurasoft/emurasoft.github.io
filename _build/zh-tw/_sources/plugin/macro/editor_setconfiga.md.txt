# Editor\_SetConfigA

變更為一個用 ANSI 字串指定的組態。您能直接用該內嵌函式或明確地發送 [EE\_SET\_CONFIGA](../message/ee_set_configa) 消息。

Editor\_SetConfigA( HWND hwnd, LPCSTR szConfigName );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_szConfigName_

> 用 ANSI 字串指定一個組態。

## 返回值

> 不使用返回值。