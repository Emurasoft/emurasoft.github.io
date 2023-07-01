# EE\_GET\_REF

檢索一個指定外掛程式的引用號。您能明確地發送該消息或用
[Editor\_GetRef](../macro/editor_getref) 內嵌函式。

EE\_GET\_REF

wParam = 0;

lParam = (LPARAM)(ATOM)atom;

## 參數

_atom_

> 指定一個指定外掛程式檔案名的 atom。

## 返回值

> 返回值是一個指定外掛程式的引用號。如果返回值為零，指定的外掛程式能從 EmEditor 上安全卸載。
