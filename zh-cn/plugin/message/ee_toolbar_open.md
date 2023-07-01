# EE\_TOOLBAR\_OPEN

打开自定义工具栏。你能明确地发送该消息或用 [Editor\_ToolbarOpen](../macro/editor_toolbaropen) 内联函数。

EE\_TOOLBAR\_OPEN

wParam = 0;

lParam = (LPARAM) (TOOLBAR\_INFO\*) pToolbarInfo;

## 参数

_pToolbarInfo_

> 指针指向 [TOOLBAR\_INFO 结构](../structure/toolbar_info)。

## 返回值

> 返回值是一个自定义工具栏 ID。如果消息失败，返回值为零。

## 支持版本

> 支持 EmEditor 7.00 或之后的版本。
