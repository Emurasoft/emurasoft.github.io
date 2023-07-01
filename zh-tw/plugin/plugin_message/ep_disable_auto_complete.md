# EP\_DISABLE\_AUTO\_COMPLETE

查詢括號/引號自動完成功能是否被禁用。這個功能由在組態屬性中的 [**亮顯 (2)** 頁面](../../dlg/properties/highlight2/index) 上的 **自動完成括號/引號標記** 核取方塊定義。

EP\_DISABLE\_AUTO\_COMPLETE

hwnd = hwndParent;

wParam = 0;

lParam = 0;

## 參數

_hwndParent_

> 外掛程式設置對話方塊的視窗控制代碼。

## 返回值

> 您必須返回 TRUE，如果自動完成功能被禁用，或 FALSE，如果自動完成功能被啟用。

## 支持版本

> 支持 EmEditor 9.00 或之後的版本。
