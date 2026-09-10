# EE_GET_TEXTW

檢索文件文字。如果文件包含超過 `0x7ffffffe` 個 UTF-16 碼元，文字會被截斷為該長度。您可以明確傳送此訊息，或使用 [Editor_GetTextW](../macro/editor_gettextw) 內嵌函式。

```
EE_GET_TEXTW
wParam = (WPARAM) (UINT) nBufferSize;
lParam = (LPARAM) (LPWSTR) szBuffer;
```

## 參數

_nBufferSize_

緩衝區的容量，以 `WCHAR` 元素數表示，包含終止的空字元（null）所需的空間。

_szBuffer_

指向接收文件文字之緩衝區的指標。

## 傳回值

傳回所需的緩衝區大小，以 `WCHAR` 元素數表示，包含終止的空字元。

如果文件包含超過 `0x7ffffffe` 個 UTF-16 碼元，傳回值為 `0x7fffffff`。若發生錯誤則傳回 0。