# Editor\_GetVersion

返回版本号。你能直接用该内联函数或明确地发送 [EE\_GET\_VERSION](../message/ee_get_version)
消息。

Editor\_GetVersion( HWND hwnd );

Editor\_GetVersionEx( HWND hwnd, int\* pnProductType );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pnProductType_

> 指定一个指针指向整数值。这个消息返回下列值之一。
>
> |     |     |
> | --- | --- |
> | VERSION\_PRO | EmEditor Professional |
> | VERSION\_STD | EmEditor Standard |

## 返回值

> 返回被乘以 1000 的版本号。
