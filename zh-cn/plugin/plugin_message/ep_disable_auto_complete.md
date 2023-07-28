# EP\_DISABLE\_AUTO\_COMPLETE

查询括号/引号自动完成功能是否被禁用。这个功能由在配置属性中的 [**高亮 (2)** 页面](../../dlg/properties/highlight2/index) 上的 **自动完成括号/引号标记** 复选框定义。

EP\_DISABLE\_AUTO\_COMPLETE

hwnd = hwndParent;

wParam = 0;

lParam = 0;

## 参数

_hwndParent_

插件设置对话框的窗口句柄。

## 返回值

你必须返回 TRUE，如果自动完成功能被禁用，或 FALSE，如果自动完成功能被启用。

## 支持版本

支持 EmEditor 9.00 或之后的版本。
