# Editor\_GetCmdID

獲得外掛程式命令 ID。您能直接用該內嵌函式或明確地發送 [EE\_GET\_CMD\_ID](../message/ee_get_cmd_id)
消息。

Editor\_GetCmdID( HWND hwnd, HINSTANCE hInstance );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_hInstance_

> 指定外掛程式的實例句柄。

## 返回值

> 返回命令 ID 來運行該外掛程式。