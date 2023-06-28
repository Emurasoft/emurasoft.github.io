# EE\_KEYBOARD\_PROP

顯示指定命令 ID 和配置的鍵盤屬性。您能明確地發送該消息或用
[Editor\_KeyboardProp](../macro/editor_keyboardprop) 內嵌函式。

EE\_KEYBOARD\_PROP

wParam = (WPARAM)(UINT)nCmdID;

lParam = (LPARAM)(LPCWSTR)pszConfigName;

## 參數

_nCmdID_

> 給鍵盤屬性上的初始選區指定命令 ID。

_pszConfigName_

> 指定 EmEditor 顯示鍵盤屬性的配置。

## 返回值

> 如果用戶在配置屬性上選擇 OK，返回值是 TRUE。如果用戶選擇 Cancel，返回值是 FALSE。