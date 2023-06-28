# Editor\_EmptyUndoBuffer

为撤消和重做命令清空缓冲区。你能直接用该内联函数或明确地发送
[EE\_EMPTY\_UNDO\_BUFFER](../message/ee_empty_undo_buffer)
消息。

Editor\_EmptyUndoBuffer( HWND hwnd );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

## 返回值

> 不使用返回值。