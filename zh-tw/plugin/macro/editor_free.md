# Editor\_Free

釋放一個指定的外掛程式。您能直接用該內嵌函式或明確地發送 [EE\_FREE](../message/ee_free) 消息。

Editor\_Free( HWND hwnd, ATOM atom );

## 參數

_hwnd_

通過被查詢的 Unicode 指定字元代碼。S

_atom_

指定一個指定外掛程式檔案名的 atom。

## 返回值

如果外掛程式被釋放，返回值是 TRUE。如果外掛程式沒有被釋放，返回值是 FALSE。
