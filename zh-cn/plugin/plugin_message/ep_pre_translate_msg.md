# EP\_PRE\_TRANSLATE\_MSG

在每一条 Windows 消息被翻译之前召集。

EP\_PRE\_TRANSLATE\_MSG

hwnd = hwndView;

wParam = 0;

lParam = (LPARAM) (MSG\*) pMsg;

## 参数

_hwndView_

> EmEditor 查看的窗口句柄。

_pMsg_

> 指针指向窗口消息在被翻译之前。

## 返回值

> 如果返回值是 TRUE，消息不会被继续翻译或发送。如果返回值是 FALSE，消息会被继续翻译或发送。

## 支持版本

> Supported on Version 6.00 或之后的版本。
