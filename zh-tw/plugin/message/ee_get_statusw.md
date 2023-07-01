# EE\_GET\_STATUSW

檢索顯示在狀態列上的 Unicode 文本。您能明確地發送該消息或用 [Editor\_GetStatusW](../macro/editor_getstatusw) 內嵌函式。

EE\_GET\_STATUSW

wParam = nBufSize;

lParam = (LPARAM) (LPWSTR) szStatus;

## 參數

_nBufSize_

> 用字符數指定緩沖區的大小，包括終止空字符。您能指定 0 如果 _szStatus_ 為空。如果緩沖區大小不夠， _szStatus_ 不會檢索任何字符串。

_szStatus_

> 指定要檢索字符串的緩沖區。如果指定值為是空 (NULL)，返回足夠的緩沖區大小來檢索字符串。

## 返回值

> 返回 TRUE 如果當前標志允許或阻止在 EmEditor 中重新繪制變更。否則，返回 FALSE。
