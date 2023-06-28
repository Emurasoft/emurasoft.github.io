# EE\_GET\_CMD\_ID

獲得外掛程式命令 ID。您能明確地發送該消息或用 [Editor\_GetCmdID](../macro/editor_getcmdid)
內嵌函式。

EE\_GET\_CMD\_ID

wParam = 0;

lParam = (LPARAM) (HINSTANCE) hInstance

## 參數

_hInstance_

> 指定外掛程式的實例句柄。

## 返回值

> 返回命令 ID 來運行該外掛程式。