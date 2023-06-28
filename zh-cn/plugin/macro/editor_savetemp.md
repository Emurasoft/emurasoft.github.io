# Editor\_SaveTemp

保存临时文本。你能直接用该内联函数或明确地发送 [EE\_EDIT\_TEMP](../message/ee_edit_temp)
消息。

Editor\_SaveTemp( HWND hwnd, UINT nEditID );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nEditID_

> 指定你想要保持的临时文本的 ID。

## 返回值

> 返回值是新文档的 ID。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。