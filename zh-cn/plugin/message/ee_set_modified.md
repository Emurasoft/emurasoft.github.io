# EE\_SET\_MODIFIED

变更文本的修改状态。你能明确地发送该消息或用
[Editor\_SetModified](../macro/editor_setmodified) 内联函数。

```
EE_SET_MODIFIED
wParam = (WPARAM) (BOOL) bModified;
lParam = 0;
```

## 参数

_bModified_

TRUE，把状态变更为修改过，或 FALSE，把状态变更为未经修改。

## 返回值

不使用返回值。
