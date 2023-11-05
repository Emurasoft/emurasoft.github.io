# EE\_SET\_OUTLINE\_ARRAY

為指定的多行設置大綱級別。您能明確地發送該消息或用
[Editor\_SetOutlineArray](../macro/editor_setoutlinearray) 內嵌函式。

```
EE_SET_OUTLINE_ARRAY
wParam = (WPARAM) 0;
lParam = (LPARAM) (OUTLINE_ARRAY_INFO*) pOutlineArrayInfo;
```

## 參數

_pOutlineArrayInfo_

指針指向一個 [OUTLINE\_ARRAY\_INFO](../structure/outline_array_info) 結構。

## 返回值

返回值是 FALSE 如果沒有變更。否則，返回值是 TRUE。

## 支持版本

支持 EmEditor 13 或之後的版本。
