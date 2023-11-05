# EE\_EDIT\_COLUMN

移動，復制，刪除，或合併目前的 CSV 文檔中的指定欄。你能明確地發送該消息或用 [Editor\_EditColumn](../macro/editor_editcolumn) 內嵌函式。

```
EE_EDIT_COLUMN
wParam = (WPARAM)(EDIT_COLUMN_INFO*)pInfo;
lParam = 0;
```

## 參數

_pInfo_

指定指針指向 [EDIT\_COLUMN\_INFO](../structure/edit_column_info) 結構。

## 返回值

如果成功，返回值為 S\_OK。

## 版本

支持 EmEditor Professional 19.7 或之後的版本。
