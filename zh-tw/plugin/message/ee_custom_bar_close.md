# EE\_CUSTOM\_BAR\_CLOSE

關閉自訂分欄。您能明確地發送該消息或用
[Editor\_CustomBarClose](../macro/editor_custombarclose) 內嵌函式。

EE\_CUSTOM\_BAR\_CLOSE

wParam = nCustomBarID;

lParam = 0;

## 參數

_nCustomBarID_

> 指定要關閉的自訂分欄。這是從 EE\_CUSTOM\_BAR\_OPEN 消息中得到的返回值。

## 返回值

> 如果消息成功，返回值為 TRUE。如果消息不成功，返回值是 FALSE。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。