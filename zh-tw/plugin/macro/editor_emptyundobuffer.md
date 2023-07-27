# Editor\_EmptyUndoBuffer

為復原和重做命令清空緩沖區。您能直接用該內嵌函式或明確地發送
[EE\_EMPTY\_UNDO\_BUFFER](../message/ee_empty_undo_buffer)
消息。

Editor\_EmptyUndoBuffer( HWND hwnd );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

## 返回值

不使用返回值。
