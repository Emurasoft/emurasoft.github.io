# EE\_UNPIVOT

通過壓平合併 CSV 數據將欄轉換為列。你能明確地發送該消息或用 [Editor\_Unpivot](../macro/editor_unpivot) 內嵌函式。

```
EE_UNPIVOT
wParam = (WPARAM)(UNPIVOT*)pInfo;
lParam = 0;
```

## 參數

_pInfo_

指定指針指向 [UNPIVOT\_INFO](../structure/pivot_table_info) 結構。

## 返回值

如果失敗，則返回值為負值。

## 支持版本

支持 EmEditor Professional 21.4 或之後的版本。
