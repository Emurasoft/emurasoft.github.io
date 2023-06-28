# Editor\_DocSetConfigW

把指定文檔變更為一個用 Unicode 字串指定的組態。您能直接用該內嵌函式或明確地發送 [EE\_SET\_CONFIGW](../message/ee_set_configw) 消息。

Editor\_SetConfigW( HWND hwnd, int iDoc, LPCWSTR szConfigName );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_iDoc_

> 指定目標文檔的索引。如果指定值為 -1，目前的活動文檔會被設為目標文檔。

_szConfigName_

> 用 Unicode 字串指定一個組態。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 5.00 或之後的版本。