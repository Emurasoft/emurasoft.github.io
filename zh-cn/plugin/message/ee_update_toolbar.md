# EE\_UPDATE\_TOOLBAR

在工具栏中更新一个按钮的状态。你能明确地发送该消息或用 [Editor\_UpdateToolbar](../macro/editor_updatetoolbar) 内联函数。

```
EE_UPDATE_TOOLBAR
wParam = (WPARAM) (UINT) nCmdID;
lParam = 0;
```

## 参数

_nCmdID_

状态被询问的命令的识别符。查看
[命令 ID](../cmdid/index)。

## 返回值

不使用返回值。
