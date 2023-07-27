# Editor\_ExecCommand

执行一个指定的命令。你能直接用该内联函数或明确地发送 [EE\_EXEC\_COMMAND](../message/ee_exec_command)
消息。

Editor\_ExecCommand( HWND hwnd, UINT nCmdID );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nCmdID_

要执行的命令的识别符。请查看 [命令 ID](../cmdid/index)。

## 返回值

不使用返回值。
