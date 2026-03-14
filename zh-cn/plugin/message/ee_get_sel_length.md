# EE_GET_SEL_LENGTH

检索所选文本的长度。你可以显式发送此消息，或使用 [Editor_GetSelLength](../macro/editor_getsellength) 内联函数。

```
EE_GET_SEL_LENGTH
wParam = (WPARAM) (size_t) nMaxLen
lParam = (LPARAM)0
```

## 参数

_nMaxLen_

指定最大长度。如果长度超过此值，则返回此值。

## 返回值

返回值为所选文本的长度。如果长度大于 LONG_MAX，则返回值为 LONG_MAX。

## 版本

支持 EmEditor Professional 26.1 或更新版本。