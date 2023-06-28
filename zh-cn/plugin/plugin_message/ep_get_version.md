# EP\_GET\_VERSION

检索插件版本。

EP\_GET\_VERSION

hwnd = hwndParent;

wParam = cb;

lParam = szVersion;

## 参数

_hwndParent_

> 插件设置对话框的窗口句柄。

_cb_

> 指定要复制到缓冲区的最大字符数，包括 NULL 字符。

_szVersion_

> 指针指向会接收文本的缓冲区。

## 返回值

> 返回值是一个能接收文本的缓冲区的必需大小。