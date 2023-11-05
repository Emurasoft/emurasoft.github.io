# EE\_TOOLBAR\_OPEN

打開自訂工具列。您能明確地發送該消息或用 [Editor\_ToolbarOpen](../macro/editor_toolbaropen) 內嵌函式。

```
EE_TOOLBAR_OPEN
wParam = 0;
lParam = (LPARAM) (TOOLBAR_INFO*) pToolbarInfo;
```

## 參數

_pToolbarInfo_

指針指向 [TOOLBAR\_INFO 結構](../structure/toolbar_info)。

## 返回值

返回值是一個自訂工具列 ID。如果消息失敗，返回值為零。

## 支持版本

支持 EmEditor 7.00 或之後的版本。
