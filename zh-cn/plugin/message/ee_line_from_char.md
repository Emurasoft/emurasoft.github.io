# EE\_LINE\_FROM\_CHAR

检索包含指定字符索引（序列位置）的行的索引。一个字符索引是以零为初始值的整个文本起始处的字符的索引。你能明确地发送该消息或用
[Editor\_LineFromChar](../macro/editor_linefromchar)
内联函数。

```
EE_LINE_FROM_CHAR
wParam = (WPARAM) (int) nLogical;
lParam = (LPARAM) (UINT) nSerialIndex;
```

## 参数

_nLogical_

指定下列值之一。

| 值 | 含义 |
| --- | --- |
| POS\_VIEW | 显示坐标 |
| POS\_LOGICAL\_A | 逻辑坐标（把双字节字符计为两个） |
| POS\_LOGICAL\_W | 逻辑坐标（把双字节字符计为一个） |

_nSerialIndex_

指定被包含在要被检索的行号中的字符的字符索引。如果参数是 -1，EE\_LINE\_FROM\_CHAR 检索当前行（光标所在行）的行号。

## 返回值

返回值是从零开始的、包含由 _nSerialIndex_ 指定的字符索引的行号。
