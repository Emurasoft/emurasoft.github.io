# EE\_GET\_VERSION

返回版本号。你能明确地发送该消息或用 [Editor\_GetVersion](../macro/editor_getversion)
内联函数。

```
EE_GET_VERSION
wParam = pnProductType;
lParam = 0;
```

## 参数

_pnProductType_

指定一个指针指向整数值。这个消息返回下列值之一。

|     |     |
| --- | --- |
| VERSION\_PRO | EmEditor Professional |
| VERSION\_STD | EmEditor Standard |

## 返回值

返回被乘以 10000 的版本号。例如，如果版本号是25.1.907，返回值将是251907。
