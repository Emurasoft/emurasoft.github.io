# Editor\_SetOutlineLevel

为指定的逻辑行设置大纲级别。你能直接用该内联函数或明确地发送 [EE\_SET\_OUTLINE\_LEVEL](../message/ee_set_outline_level) 消息。

Editor\_SetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine, int nLevel );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nLogicalLine_

> 指定一个逻辑行。

_nLevel_

> 指定一个大纲级别。

## 返回值

> 返回值是旧的指定逻辑行的大纲级别。如果发生错误，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。
