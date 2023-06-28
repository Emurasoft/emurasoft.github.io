# EP\_GET\_INFO

檢索有關外掛程式的信息。

EP\_GET\_INFO

hwnd = hwndParent;

wParam = flag;

lParam = 0;

## 參數

_hwndParent_

> EmEditor 框架視窗的視窗控制代碼。

_標志_

> 指定被請求的信息類型。它是下列值之一。
>
> | 值 | 含義 |
> | --- | --- |
> | EPGI\_ALLOW\_OPEN\_SAME\_GROUP | 返回 TRUE 如果該外掛程式允許 EmEditor 在同一個群組中打開一個新檔案。 |
> | EPGI\_ALLOW\_MULTIPLE\_INSTANCES | 返回 TRUE 如果外掛程式支持多個實例。如果外掛程式被允許在多于一個框架中同時運行，這個消息會返回 TRUE。注意全局變量會被分享當多個實例運行時。 |
> | EPGI\_MAX\_EE\_VERSION | 返回支持的 EmEditor 的最新版本號 \* 1000。 |
> | EPGI\_MIN\_EE\_VERSION | 返回支持的 EmEditor 最舊的版本號 \* 1000。 |
> | EPGI\_SUPPORT\_EE\_PRO | 返回 TRUE 如果支持 EmEditor Professional。 |
> | EPGI\_SUPPORT\_EE\_STD | 返回 TRUE 如果支持 EmEditor Standard。 |

## 返回值

> 返回值取決于標志參數。

## 支持版本

> 支持 EmEditor 5.00 或之後的版本。