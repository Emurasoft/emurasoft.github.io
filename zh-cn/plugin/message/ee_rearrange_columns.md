# EE\_REARRANGE\_COLUMNS

重排 CSV 列。你能明确地发送该消息或用 [Editor\_RearrangeColumns](../macro/editor_rearrangecolumns) 内联函数。

EE\_REARRANGE\_COLUMNS

wParam = (WPARAM) (REARRANGE\_COLULMNS\_INFO\*)pInfo;

lParam = 0;

## 参数

_pInfo_

指定指针指向 [REARRANGE\_COLUMNS\_INFO](../structure/rearrange_columns_info) 结构。

## 返回值

如果消息成功，则返回值为零。如果消息失败，则返回值非零。

## 版本

支持 EmEditor Professional v22.1 或之后的版本。
