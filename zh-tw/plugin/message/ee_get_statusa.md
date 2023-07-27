# EE\_GET\_STATUSA

檢索顯示在狀態列上的 ANSI 文本。您能明確地發送該消息或用 [Editor\_GetStatusA 內嵌函式](../macro/editor_getstatusa)。

EE\_GET\_STATUSA

wParam = nBufLen;

lParam = (LPARAM) (LPSTR) szMessage;

## 參數

_nBufLen_

用字符數指定緩沖區的大小，包括終止空字符。您能指定 0 如果 _szMessage_ 為空。如果緩沖區大小不夠， _szMessage_ 不會檢索任何字符串。

_szMessage_

指定要檢索字符串的緩沖區。如果指定的是空 (NULL)，返回足夠的緩沖區大小來檢索字符串。

## 返回值

返回 TRUE 如果當前標志允許或阻止在 EmEditor 中重新繪制變更。否則，返回 FALSE。
