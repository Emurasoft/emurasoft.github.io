# EP\_GET\_INFO

检索有关插件的信息。

EP\_GET\_INFO

hwnd = hwndParent;

wParam = flag;

lParam = 0;

## 参数

_hwndParent_

> EmEditor 框架窗口的窗口句柄。

_标志_

> 指定被请求的信息类型。它是下列值之一。
>
> | 值 | 含义 |
> | --- | --- |
> | EPGI\_ALLOW\_OPEN\_SAME\_GROUP | 返回 TRUE 如果该插件允许 EmEditor 在同一个群组中打开一个新文件。 |
> | EPGI\_ALLOW\_MULTIPLE\_INSTANCES | 返回 TRUE 如果插件支持多个实例。如果插件被允许在多于一个框架中同时运行，这个消息会返回 TRUE。注意全局变量会被分享当多个实例运行时。 |
> | EPGI\_MAX\_EE\_VERSION | 返回支持的 EmEditor 最新的版本号 \* 1000。 |
> | EPGI\_MIN\_EE\_VERSION | 返回支持的 EmEditor 最旧的版本号 \* 1000。 |
> | EPGI\_SUPPORT\_EE\_PRO | 返回 TRUE 如果支持 EmEditor Professional。 |
> | EPGI\_SUPPORT\_EE\_STD | 返回 TRUE 如果支持 EmEditor Standard。 |

## 返回值

> 返回值取决于标志参数。

## 支持版本

> 支持 EmEditor 5.00 或之后的版本。
