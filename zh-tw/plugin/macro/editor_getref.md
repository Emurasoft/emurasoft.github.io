# Editor\_GetRef

檢索一個指定外掛程式的引用號。您能直接用該內嵌函式或明確地發送 [EE\_GET\_REF](../message/ee_get_ref) 消息。

Editor\_GetRef( HWND hwnd, ATOM atom );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_atom_

指定一個指定外掛程式檔案名的 atom。

## 返回值

返回值是一個指定外掛程式的引用號。如果返回值為零，指定的外掛程式能從 EmEditor 上安全卸載。
