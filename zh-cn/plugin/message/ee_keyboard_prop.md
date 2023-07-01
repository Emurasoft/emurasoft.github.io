# EE\_KEYBOARD\_PROP

显示指定命令 ID 和配置的键盘属性。你能明确地发送该消息或用
[Editor\_KeyboardProp](../macro/editor_keyboardprop) 内联函数。

EE\_KEYBOARD\_PROP

wParam = (WPARAM)(UINT)nCmdID;

lParam = (LPARAM)(LPCWSTR)pszConfigName;

## 参数

_nCmdID_

> 给键盘属性上的初始选区指定命令 ID。

_pszConfigName_

> 指定 EmEditor 显示键盘属性的配置。

## 返回值

> 如果用户在配置属性上选择 OK，返回值是 TRUE。如果用户选择 Cancel，返回值是 FALSE。
