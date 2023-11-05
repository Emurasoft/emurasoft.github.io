# EE\_GET\_CMD\_ID

获得插件命令 ID。你能明确地发送该消息或用 [Editor\_GetCmdID](../macro/editor_getcmdid)
内联函数。

```
EE_GET_CMD_ID
wParam = 0;
lParam = (LPARAM) (HINSTANCE) hInstance
```

## 参数

_hInstance_

指定插件的实例句柄。

## 返回值

返回命令 ID 来运行该插件。
