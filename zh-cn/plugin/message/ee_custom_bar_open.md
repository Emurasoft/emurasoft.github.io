# EE\_CUSTOM\_BAR\_OPEN

打开自定义分栏。如果在发送该消息前已经打开了一个自定义分栏，EmEditor 会关闭该自定义分栏并打开一个新的自定义分栏。你能明确地发送该消息或用 [Editor\_CustomBarOpen](../macro/editor_custombaropen) 内联函数。

EE\_CUSTOM\_BAR\_OPEN

wParam = 0;

lParam = (LPCTSTR) (LPCTSTR) pCustomBarInfo;

## 参数

_pCustomBarInfo_

> 指针指向 [CUSTOM\_BAR\_INFO 结构](../structure/custom_bar_info)。

## 返回值

> 返回值是一个自定义分栏 ID。这个 ID 是必要的当用 EE\_CUSTOM\_BAR\_CLOSE 消息来关闭该自定义分栏时。如果消息不成功，返回值则是零。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。
