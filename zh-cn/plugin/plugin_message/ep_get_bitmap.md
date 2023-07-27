# EP\_GET\_BITMAP

为显示在工具栏上的插件检索位图资源 ID 的各种大小与颜色深度。

EP\_GET\_BITMAP

hwnd = hwndParent;

wParam = flags;

lParam = 0;

## 参数

_hwndParent_

EmEditor 框架窗口的窗口句柄。

_flags_

指定要检索的一个位图的位图大小和颜色深度。它可以是下列标志的组合。

| 值 | 含义 |
| --- | --- |
| BITMAP\_SMALL | 小位图 (16x16 像素) |
| BITMAP\_LARGE | 大位图 (24x24 像素) |
| BITMAP\_16\_COLOR | 16 色位图 |
| BITMAP\_24BIT\_COLOR | 24 位色彩（真彩色）位图 |
| BITMAP\_256\_COLOR | 256 色位图 |
| BITMAP\_DEFAULT | 默认状态位图 |
| BITMAP\_DISABLED | 停用状态位图 |
| BITMAP\_HOT | 热态位图 |

## 返回值

你必须为所要求的大小和颜色深度返回一个位图资源 ID。如果返回值是零，EmEditor 会用 GetBitmapID 导出函数来检索小 16 色位图。
