# EE\_SET\_MODIFIED

變更文本的修改狀態。您能明確地發送該消息或用
[Editor\_SetModified](../macro/editor_setmodified) 內嵌函式。

EE\_SET\_MODIFIED

wParam = (WPARAM) (BOOL) bModified;

lParam = 0;

## 參數

_bModified_

> TRUE，把狀態變更為修改過，或 FALSE，把狀態變更為未經修改。

## 返回值

> 不使用返回值。
