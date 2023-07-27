# Editor\_DocGetConfigW

為指定的文檔檢索選取的組態名稱并把它作為一個 Unicode 字串。您能直接用該內嵌函式或明確地發送 [EE\_GET\_CONFIGW](../message/ee_get_configw) 消息。

Editor\_DocGetConfigW( HWND hwnd, int iDoc, LPWSTR szConfigName );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_iDoc_

指定目標文檔的索引。如果指定值為 -1，目前的活動文檔會被設為目標文檔。

_szConfigName_

指定會接收組態名稱的一個緩沖區。緩沖區大小必須至少是MAX\_CONFIG\_NAME 位元。

## 返回值

不使用返回值。

## 支持版本

支持 EmEditor 5.00 或之後的版本。
