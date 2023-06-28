# Editor\_SetOutlineArray

為指定的多行設置大綱級別。您能直接用該內嵌函式或明確地發送
[EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) 消息。

Editor\_SetOutlineArray( HWND hwnd, INT\_PTR nStartLine, INT\_PTR nCount, BYTE\* pLevelData );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nStartLine_

> 指定多行的首行。

_nCount_

> 指定多行的行數。

_pLevelData_

> 指定決定大綱級別的位元數組。

## 返回值

> 返回值是 FALSE 如果沒有變更。否則，返回值是 TRUE。

## 支持版本

> 支持 EmEditor 13 或之後的版本。