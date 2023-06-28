# Editor\_SetOutlineLevel

為指定的邏輯行設置大綱級別。您能直接用該內嵌函式或明確地發送 [EE\_SET\_OUTLINE\_LEVEL](../message/ee_set_outline_level) 消息。

Editor\_SetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine, int nLevel );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nLogicalLine_

> 指定邏輯行。

_nLevel_

> 指定一個大綱級別。

## 返回值

> 返回值是之前的指定邏輯行的大綱級別。如果發生錯誤，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。