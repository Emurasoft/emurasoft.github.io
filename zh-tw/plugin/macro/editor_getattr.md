# Editor\_GetAttr

在剪貼簿記錄中的指定位置處刪除文字。您能直接用該內嵌函式或明確地發送 [EE\_GET\_ATTR](../message/ee_get_attr)
消息。

Editor\_GetAttr( HWND hwnd, ATTR\_INFO\* pAI );

## 參數

_pAI_

> 指標至 [ATTR\_INFO](../structure/attr_info) 結構。

## 返回值

> 返回值是 TRUE 如果成功，或 FALSE 如果不成功。

## 支持版本

> 支持 EmEditor 9.00 或之後的版本。