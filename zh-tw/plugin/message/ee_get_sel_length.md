# EE_GET_SEL_LENGTH

取得所選取文字的長度。您可以明確傳送此訊息，或使用  
[Editor_GetSelLength](../macro/editor_getsellength) 內嵌函式。

```
EE_GET_SEL_LENGTH
wParam = (WPARAM)0
lParam = (LPARAM)0
```

## 返回值

返回值為所選取文字的長度。若長度大於 LONG_MAX，則返回值會變為 LONG_MAX。

## 版本

支持 EmEditor Professional 26.1 或更新版本。