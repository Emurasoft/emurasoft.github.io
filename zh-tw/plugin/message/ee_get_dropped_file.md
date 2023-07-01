# EE\_GET\_DROPPED\_FILE

檢索最近拖放的檔案。您能明確地發送該消息或用
[Editor\_GetDroppedFile](../macro/editor_getdroppedfile) 內嵌函式。

EE\_GET\_CONFIGW

wParam = (WPARAM) (int) nIndex;

lParam = (LPARAM) (LPWSTR) pszBuf;

## 參數

_nIndex_

> 指定拖放檔案的索引。應指定從 0 開始的索引。如果指定 -1，那拖放檔案的總數會被返回。

_pszBuf_

> 指定接收拖放檔案名稱的一個緩沖區。緩沖區大小必須是 MAX\_PATH 的位元數。這個參數可以為空 (NULL)，如果 -1 在 nIndex 中被指定的話。

## 返回值

> 返回值為非零值如果拖放檔案存在在指定的索引中。如果在 nIndex 中指定 -1，返回值是拖放檔案的總數。

## 支持版本

支持 EmEditor 8.00 或之後的版本。
