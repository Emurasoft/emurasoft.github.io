# EE\_GET\_SEL\_TEXTA

檢索被選取的 ANSI 文本。您能明確地發送該消息或用 [Editor\_GetSelTextA](../macro/editor_getseltexta) 內嵌函式。

```
EE_GET_SEL_TEXTA
wParam = (WPARAM) (UINT) nBufferSize;
lParam = (LPARAM) (LPSTR) szBuffer;
```

## 參數

_nBufferSize_

用位元數指定最大的字符數來複製到緩沖區，包括空字符。

_szBuffer_

指針指向會接收文本的緩沖區。

## 返回值

如果 _nBufferSize_ 為零，那返回值是用位元數表示的一個會接收文本的緩沖區的必需大小。如果 _nBufferSize_ 為非零，不使用返回值。
