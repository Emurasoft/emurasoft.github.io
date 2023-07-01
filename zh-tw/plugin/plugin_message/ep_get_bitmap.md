# EP\_GET\_BITMAP

為顯示在工具列上的外掛程式檢索位圖資源 ID 的各種大小與顏色深度。

EP\_GET\_BITMAP

hwnd = hwndParent;

wParam = flags;

lParam = 0;

## 參數

_hwndParent_

> EmEditor 框架視窗的視窗控制代碼。

_flags_

> 指定要檢索的一個位圖的位圖大小和顏色深度。它可以是下列標志的組合。
>
> | 值 | 含義 |
> | --- | --- |
> | BITMAP\_SMALL | 小位圖 (16x16 像素) |
> | BITMAP\_LARGE | 大位圖 (24x24 像素) |
> | BITMAP\_16\_COLOR | 16 色位圖 |
> | BITMAP\_24BIT\_COLOR | 24 位色彩 (真彩色) 位圖 |
> | BITMAP\_256\_COLOR | 256 色位圖 |
> | BITMAP\_DEFAULT | 預設狀態位圖 |
> | BITMAP\_DISABLED | 停用狀態位圖 |
> | BITMAP\_HOT | 熱態位圖 |

## 返回值

> 您必須為所要求的大小和顏色深度返回一個位圖資源 ID。如果返回值是零，EmEditor 會用 GetBitmapID 導出函數來檢索小 16 色位圖。
