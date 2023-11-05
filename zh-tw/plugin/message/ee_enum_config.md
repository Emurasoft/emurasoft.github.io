# EE\_ENUM\_CONFIG

列舉可用的配置。您能明確地發送該消息或用 [Editor\_EnumConfig](../macro/editor_enumconfig) 內嵌函式。

```
EE_ENUM_CONFIG
wParam = (WPARAM) (size_t) cchBuf;
lParam = (LPARAM) (LPWSTR) pBuf;
```

## 參數

_cchBuf_

用字符數指定緩沖區大小。要注意的是兩個空字符會被添加到配置列表末尾。如果指定的數值為 0，該消息會返回檢索配置列表的必需大小。

_pBuf_

指定指針指向緩沖區來檢索配置列表。在這個緩沖區內，由一個空字符分隔的可用的配置列表會被檢索。兩個空字符會被添加到配置列表末尾。如果指定的數值為 0，pBuf 是空 (NULL)。

## 返回值

返回值是檢索配置列表的必需大小。

## 支持版本

支持 EmEditor 6.00 或之後的版本。
