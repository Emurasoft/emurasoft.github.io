# EE_GET_SEL_LENGTH

檢索選取文字的長度。您可以明確傳送此訊息，或使用 [Editor_GetSelLength](../macro/editor_getsellength) 內嵌函式。

```
EE_GET_SEL_LENGTH
wParam = (WPARAM) (size_t) nMaxLen
lParam = (LPARAM)0
```
## 參數

_nMaxLen_

指定最大長度。如果長度超過此值，則返回此值。

## 返回值

返回值為所選取文字的長度。若長度大於 LONG_MAX，則返回值會變為 LONG_MAX。

## 版本

支持 EmEditor Professional 26.1 或更新版本。