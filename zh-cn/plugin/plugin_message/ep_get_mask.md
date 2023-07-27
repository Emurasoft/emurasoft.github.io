# EP\_GET\_MASK

为在工具栏上的插件按钮检索过滤色。

EP\_GET\_MASK

hwnd = hwndParent;

wParam = flags;

lParam = 0;

## 参数

_hwndParent_

EmEditor 框架窗口的窗口句柄。

_flags_

为一个要检索的位图指定位图颜色深度。

| 值 | 含义 |
| --- | --- |
| BITMAP\_24BIT\_COLOR | 24 位色彩（真彩色）位图 |
| BITMAP\_256\_COLOR | 256 色位图 |

## 返回值

你必须为在工具栏上的插件按钮把一个过滤色返回为一个RGB( r, g, b ) 值。一个位图上的过滤色会被工具栏的颜色所替换。一个大位图的过滤色一定要与小位图的过滤色一致。同时，你不能为 16 色位图指定一个过滤色。如果返回值是零，EmEditor 会把 RGB(192,192,192) 作为一个默认的过滤色。
