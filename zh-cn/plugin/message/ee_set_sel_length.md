# EE\_SET\_SEL\_LENGTH

变更选区的字符长度。你能明确地发送该消息或用
[Editor\_SetSelLength](../macro/editor_setsellength)
内联函数。

```
EE_SET_SEL_LENGTH
wParam = (WPARAM) (UINT) nLen;
lParam = 0;
```

## 参数

_nLen_

指定选区的字符长度。换行总是计为两个字符长度 (CR+LF)。

## 返回值

不使用返回值。
