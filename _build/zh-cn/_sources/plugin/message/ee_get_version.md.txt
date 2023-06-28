# EE\_GET\_VERSION

返回版本号。你能明确地发送该消息或用 [Editor\_GetVersion](../macro/editor_getversion)
内联函数。

EE\_GET\_VERSION

wParam = pnProductType;

lParam = 0;

## 参数

_pnProductType_

> 指定一个指针指向整数值。这个消息返回下列值之一。
>
> |     |     |
> | --- | --- |
> | VERSION\_PRO | EmEditor Professional |
> | VERSION\_STD | EmEditor Standard |

## 返回值

> 返回被乘以 1000 的版本号。