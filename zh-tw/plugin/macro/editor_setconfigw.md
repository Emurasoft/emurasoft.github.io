# Editor\_SetConfigW

變更為一個用 Unicode 字串指定的組態。您能直接用該內嵌函式或明確地發送 [EE\_SET\_CONFIGW](../message/ee_set_configw) 消息。

Editor\_SetConfigW( HWND hwnd, LPCWSTR szConfigName );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_szConfigName_

用 Unicode 字串指定一個組態。

## 返回值

不使用返回值。
