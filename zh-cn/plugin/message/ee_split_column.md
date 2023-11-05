# EE\_SPLIT\_COLUMN

分割当前 CSV 文档的指定列。你能明确地发送该消息或用 [Editor\_SplitColumn](../macro/editor_splitcolumn) 内联函数。

```
EE_SPLIT_COLUMN
wParam = (WPARAM)(SPLIT_COLUMN_INFO*)pInfo;
lParam = 0;
```

## 参数

_pInfo_

指定指针指向 [SPLIT\_COLUMN\_INFO](../structure/split_column_info) 结构。

## 返回值

如果失败，返回值为负。

## 版本

支持 EmEditor Professional 19.9 或之后的版本。
