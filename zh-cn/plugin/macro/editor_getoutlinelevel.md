# Editor\_GetOutlineLevel

检索指定逻辑行的大纲级别。你能直接用该内联函数或明确地发送 [EE\_GET\_OUTLINE\_LEVEL](../message/ee_get_outline_level) 消息。

Editor\_GetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nLogicalLine_

> 指定一个逻辑行。

## 返回值

> 返回值是指定逻辑行的大纲级别。如果发生错误，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。
