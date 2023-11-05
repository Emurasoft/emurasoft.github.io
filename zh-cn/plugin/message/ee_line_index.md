# EE\_LINE\_INDEX

检索在 EmEditor 中一个指定行的第一个字符的字符索引。一个字符索引是以零为初始值的编辑控件起始处的字符的索引。你能明确地发送该消息或用 [Editor\_LineIndex](../macro/editor_lineindex) 内联函数。

```
EE_LINE_INDEX
wParam = (WPARAM) (BOOL) bLogical;
lParam = (LPARAM) (int) yLine;
```

## 参数

_bLogical_

指定 TRUE，如果行号是按逻辑坐标。指定 FALSE，如果行号是按显示坐标。

_yLine_

指定从零开始的行号。-1 代表当前行（光标所在行）的行号。

## 返回值

返回值是在 _yLine_ 参数中指定的行的字符索引。
