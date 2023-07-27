# EE\_GET\_ACTIVE\_STRING

檢索主動字串。你能明確地發送該消息或用 [Editor\_GetActiveString](../macro/editor_getactivestring) 內嵌函式。

EE\_GET\_ACTIVE\_STRING

wParam = (WPARAM) 0;

lParam = (LPARAM) (ACTIVE\_STRING\_INFO\*) pInfo;

## 參數

_pInfo_

指針指向 [ACTIVE\_STRING\_INFO](../structure/active_string_info) 結構。

## 返回值

返回要檢索包含終止 NULL 字元的主動字串所需的緩衝區字元數。

## 版本

支持 EmEditor Professional Version 16.9 或之後的版本。
