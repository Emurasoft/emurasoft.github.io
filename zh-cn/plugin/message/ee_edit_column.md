# EE\_EDIT\_COLUMN

移动，复制，删除，或合并当前 CSV 文档中的指定列。你能明确地发送该消息或用 [Editor\_EditColumn](../macro/editor_editcolumn) 内联函数。

EE\_EDIT\_COLUMN

wParam = (WPARAM)(EDIT\_COLUMN\_INFO\*)pInfo;

lParam = 0;

## 参数

_pInfo_

> 指定指针指向 [EDIT\_COLUMN\_INFO](../structure/edit_column_info) 结构。

## 返回值

> 如果成功，返回值为 S\_OK。

## 版本

> 支持 EmEditor Professional 19.7 或之后的版本。
