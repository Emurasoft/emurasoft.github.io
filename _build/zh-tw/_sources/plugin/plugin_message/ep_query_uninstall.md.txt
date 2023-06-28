# EP\_QUERY\_UNINSTALL

查詢外掛程式是否被卸載。

EP\_QUERY\_UNINSTALL

hwnd = hwndParent;

wParam = 0;

lParam = 0;

## 參數

_hwndParent_

> 外掛程式設置對話方塊的視窗控制代碼。

## 返回值

> 如果該外掛程式能被卸載，返回值是 TRUE。如果該外掛程式不能被卸載，返回值是 FALSE。