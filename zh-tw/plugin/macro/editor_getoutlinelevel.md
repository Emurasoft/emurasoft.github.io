# Editor\_GetOutlineLevel

檢索指定邏輯行的大綱級別。您能直接用該內嵌函式或明確地發送 [EE\_GET\_OUTLINE\_LEVEL](../message/ee_get_outline_level) 消息。

Editor\_GetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nLogicalLine_

> 指定邏輯行。

## 返回值

> 返回值是指定邏輯行的大綱級別。如果發生錯誤，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。
