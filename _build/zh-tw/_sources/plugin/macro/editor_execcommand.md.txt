# Editor\_ExecCommand

執行一個指定的命令。您能直接用該內嵌函式或明確地發送 [EE\_EXEC\_COMMAND](../message/ee_exec_command)
消息。

Editor\_ExecCommand( HWND hwnd, UINT nCmdID );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nCmdID_

> 要執行的命令的識別符。請檢視 [命令 ID](../cmdid/index)。

## 返回值

> 不使用返回值。