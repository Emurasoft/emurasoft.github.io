# Editor\_GetActiveString

檢索主動字串。你能用這個內嵌函式或明確地發送 [EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) 消息。

Editor\_GetActiveString( HWND hwnd, ACTIVE\_STRING\_INFO\* pInfo );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pTipInfo_

> 指針指向 [ACTIVE\_STRING\_INFO](../structure/active_string_info) 結構。

## 返回值

> 返回要檢索包含終止 NULL 字元的主動字串所需的緩衝區字元數。

## 版本

> 支持 EmEditor Professional 16.9 或之後的版本。