# EE\_SET\_CELL

在指定单元格内设置文本。你能明确地发送这条消息或用 [Editor\_SetCell](../macro/editor_setcell) 内联函数。

```
EE_SET_CELL
wParam = (WPARAM) (GET_CELL_INFO*) pGetCellInfo;
lParam = (LPARAM) (LPWSTR) szString;
```

## 参数

_pGetCellInfo_

指针指向 [GET\_CELL\_INFO](../structure/get_cell_info) 结构。

_szString_

指针指向要接收文本的缓冲区。

## 返回值

如果成功，返回值为零或正数值，如果失败，返回负数值。
