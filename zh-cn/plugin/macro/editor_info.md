# Editor\_Info

检索或设置用于 EmEditor 的信息参数之一的值。你能直接用该内联函数或明确地发送
[EE\_INFO](../message/ee_info) 消息。

Editor\_Info( HWND hwnd, int nCmd, LPARAM lParam );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nCmd_

指定要检索或设置的参数。命令条目请参考 [EE\_INFO](../message/ee_info) 消息。

_lParam_

取决于指定的参数。

## 返回值

取决于指定的参数。

## 支持版本

支持 EmEditor 3.00 或之后的版本。
