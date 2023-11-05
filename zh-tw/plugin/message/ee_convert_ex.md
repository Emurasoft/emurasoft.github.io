# EE\_CONVERT\_EX

轉換字元。你能明確地發送該消息或用 [Editor\_Convert](../macro/editor_convert) 內嵌函式。

```
EE_CONVERT_EX
wParam = (WPARAM) (CONVERT_INFO*)pInfo;
lParam = 0;
```

## 參數

_pInfo_

指定指針指向 [CONVERT\_INFO](../structure/convert_info) 結構。

## 返回值

如果消息成功，返回值為非零。如果消息失敗，返回值為零。

## 版本

支持 EmEditor Professional 22.1 或之後的版本。
