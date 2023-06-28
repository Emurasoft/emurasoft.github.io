# EP\_PRE\_TRANSLATE\_MSG

在每一條 Windows 消息被翻譯之前召集。

EP\_PRE\_TRANSLATE\_MSG

hwnd = hwndView;

wParam = 0;

lParam = (LPARAM) (MSG\*) pMsg;

## 參數

_hwndView_

> EmEditor 檢視的視窗控制代碼。

_pMsg_

> 指針指向視窗消息在被翻譯之前。

## 返回值

> 如果返回值是 TRUE，消息不會被繼續翻譯或發送。如果返回值是 FALSE，消息會被繼續翻譯或發送。

## 支持版本

> Supported on Version 6.00 或之後的版本。