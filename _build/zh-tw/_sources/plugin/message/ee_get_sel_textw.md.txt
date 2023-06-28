# EE\_GET\_SEL\_TEXTW

檢索被選取的 Unicode 文本。您能明確地發送該消息或用 [Editor\_GetSelTextW](../macro/editor_getseltextw) 內嵌函式。

EE\_GET\_SEL\_TEXTW

wParam = (WPARAM) (UINT) nBufferSize;

lParam = (LPARAM) (LPWSTR) szBuffer;

## 參數

_nBufferSize_

> 用單詞數指定最大字符數來複製到緩沖區，包括空字符。

_szBuffer_

> 指針指向會接收文本的緩沖區。

## 返回值

> 如果 _nBufferSize_ 為零，那返回值是用位元數表示的一個會接收文本的緩沖區的必需大小。如果 _nBufferSize_ 為非零，不使用返回值。