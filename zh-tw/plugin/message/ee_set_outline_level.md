# EE\_SET\_OUTLINE\_LEVEL

為指定的邏輯行設置大綱級別。您能明確地發送該消息或用 [Editor\_SetOutlineLevel](../macro/editor_setoutlinelevel) 內嵌函式。

EE\_SET\_OUTLINE\_LEVEL

wParam = (WPARAM) (INT\_PTR) nLogicalLine;

lParam = (LPARAM) (int) nLevel;

## 參數

_nLogicalLine_

指定邏輯行。

_nLevel_

指定一個大綱級別。

## 返回值

返回值是舊的指定邏輯行的大綱級別。如果發生錯誤，返回值是 -1。

## 支持版本

支持 EmEditor 6.00 或之後的版本。
