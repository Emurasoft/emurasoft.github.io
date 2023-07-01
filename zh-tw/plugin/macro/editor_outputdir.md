# Editor\_OutputDir

為輸出列設置目前的目錄。您能直接用該內嵌函式或明確地發送 [EE\_OUTPUT\_DIR](../message/ee_output_dir) 消息。

Editor\_OutputDir( HWND hwnd, LPCWSTR szCurrDir );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_szCurrDir_

> 指定目前的目錄。該信息是必需的如果文字含有一個只能從目前的目錄上跳轉的、可點擊的相對路徑。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。
