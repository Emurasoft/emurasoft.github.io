# EE\_SET\_STATUSA

在狀態列上顯示一條 ANSI 消息。您能明確地發送該消息或用 [Editor\_SetStatusA](../macro/editor_setstatusa) 內嵌函式。

```
EE_SET_STATUSA
wParam = 0;
lParam = (LPARAM) (LPCSTR) szStatus;
```

## 參數

_szStatus_

指定要顯示在狀態列上的消息文本。

## 返回值

不使用返回值。
