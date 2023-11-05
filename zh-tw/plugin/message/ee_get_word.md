# EE\_GET\_WORD

檢索光標位置處的一個單詞。您能明確地發送該消息或用 [Editor\_GetWord](../macro/editor_getword) 內嵌函式。

```
EE_GET_WORD
wParam = (WPARAM) (UINT) nBufferSize;
lParam = (LPARAM) (LPWSTR) szBuffer;
```

## 參數

_nBufferSize_

用字符數指定複製到緩沖區的最大字符數，包括空字符。

_szBuffer_

指針指向會接收文本的緩沖區。

## 返回值

如果 _nBufferSize_ 是零，返回值是能接收文本的緩沖區的必需的大小字符數。如果 _nBufferSize_ 不是零，不使用返回值。

## 支持版本

支持 EmEditor 10.00 或之後的版本。
