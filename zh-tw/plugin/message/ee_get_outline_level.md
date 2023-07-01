# EE\_GET\_OUTLINE\_LEVEL

檢索指定邏輯行的大綱級別。您能明確地發送該消息或用 [Editor\_GetOutlineLevel](../macro/editor_getoutlinelevel) 內嵌函式。

EE\_GET\_OUTLINE\_LEVEL

wParam = (WPARAM) (INT\_PTR) nLogicalLine;

lParam = 0;

## 參數

_nLogicalLine_

> 指定邏輯行。

## 返回值

> 返回值是指定邏輯行的大綱級別。如果發生錯誤，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。
