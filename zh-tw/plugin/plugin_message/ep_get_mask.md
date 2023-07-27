# EP\_GET\_MASK

為在工具列上的外掛程式按鈕檢索過濾色。

EP\_GET\_MASK

hwnd = hwndParent;

wParam = flags;

lParam = 0;

## 參數

_hwndParent_

EmEditor 框架視窗的視窗控制代碼。

_flags_

為一個要檢索的位圖指定位圖顏色深度。

| 值 | 含義 |
| --- | --- |
| BITMAP\_24BIT\_COLOR | 24 位色彩 (真彩色) 位圖 |
| BITMAP\_256\_COLOR | 256 色位圖 |

## 返回值

您必須為在工具列上的外掛程式按鈕把一個過濾色返回為一個RGB( r, g, b ) 值。一個位圖上的過濾色會被工具列的顏色所取代。一個大位圖的過濾色一定要與小位圖的過濾色一致。同時，您不能為 16 色位圖指定一個過濾色。如果返回值是零，EmEditor 會把 RGB(192,192,192) 作為一個預設的過濾色。
