# Editor\_DocGetModified

檢索指定文檔的文字的修改狀態。您能直接用該內嵌函式或明確地發送 [EE\_GET\_MODIFIED](../message/ee_get_modified) 消息。

Editor\_DocGetModified( HWND hwnd, int iDoc );

Editor\_DocGetModified( HWND hwnd, HEEDOC hDoc );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_iDoc_

指定目標文檔的索引。如果指定值為 -1，目前的活動文檔會被設為目標文檔。

_hDoc_

指定目標文件的控點。如果指定 NULL，則目前使用中的文件將成為目標。

## 返回值

如果文字被修改，返回值是 TRUE。如果文字沒有被修改，返回值是 FALSE。

## 支持版本

支持 EmEditor 5.00 或之後的版本。
