# EE\_TOOLBAR\_SHOW

顯示或隱藏一個自訂工具列。您能明確地發送該消息或用 [Editor\_ToolbarShow](../macro/editor_toolbarshow) 內嵌函式。

```
EE_TOOLBAR_SHOW
(UINT)wParam = nToolbarID
(BOOL)lParam = bVisible
```

## 參數

_nToolbarID_

指定要關閉的工具列。這會是 EE\_TOOLBAR\_OPEN 消息的返回值。

_bVisible_

指定 TRUE 如果要顯示工具列，或 FALSE，如果要隱藏工具列。

## 返回值

如果消息成功并且工具列狀態被改變，返回值是 TRUE。如果消息不成功或工具列狀態沒有更改，返回值是 FALSE。

## 支持版本

Supported on EmEditor Professional Version 7.00 或之後的版本。
