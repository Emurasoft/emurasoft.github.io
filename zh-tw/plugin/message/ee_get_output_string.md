# EE\_GET\_OUTPUT\_STRING

檢索輸出列中的文本。您能明確地發送該消息或用 [Editor\_GetOutputString](../macro/editor_getoutputstring) 內嵌函式。

```
EE_GET_OUTPUT_STRING
wParam = (WPARAM) (UINT) cchBuf;
lParam = (LPARAM) (LPWSTR) pBuf;
```

## 參數

_cchBuf_

用位元數指定緩沖區大小，包括終止空字符。

_pBuf_

指定指針指向接收文本的緩沖區。

## 返回值

返回值是用來接收文本的緩沖區大小位元數，包括終止空字符。

## 支持版本

支持 EmEditor 9.00 或之後的版本。
