# EE\_TOOLBAR\_SHOW

显示或隐藏一个自定义工具栏。你能明确地发送该消息或用 [Editor\_ToolbarShow](../macro/editor_toolbarshow) 内联函数。

```
EE_TOOLBAR_SHOW
(UINT)wParam = nToolbarID
(BOOL)lParam = bVisible
```

## 参数

_nToolbarID_

指定要关闭的工具栏。这会是 EE\_TOOLBAR\_OPEN 消息的返回值。

_bVisible_

指定 TRUE 如果要显示工具栏，或 FALSE，如果要隐藏工具栏。

## 返回值

如果消息成功并且工具栏状态被改变，返回值是 TRUE。如果消息不成功或工具栏状态没有更改，返回值是 FALSE。

## 支持版本

Supported on EmEditor Professional Version 7.00 或之后的版本。
