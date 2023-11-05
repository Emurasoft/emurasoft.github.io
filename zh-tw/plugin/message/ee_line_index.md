# EE\_LINE\_INDEX

檢索在 EmEditor 中一個指定行的第一個字符的字符索引。一個字符索引是以零為初始值的編輯控件起始處的字符的索引。您能明確地發送該消息或用 [Editor\_LineIndex](../macro/editor_lineindex) 內嵌函式。

```
EE_LINE_INDEX
wParam = (WPARAM) (BOOL) bLogical;
lParam = (LPARAM) (int) yLine;
```

## 參數

_bLogical_

指定 TRUE，如果行號是按邏輯坐標。指定 FALSE，如果行號是按顯示坐標。

_yLine_

指定從零開始的行號。-1 代表當前行 (光標所在行) 的行號。

## 返回值

返回值是在 _yLine_ 參數中指定的行的字符索引。
