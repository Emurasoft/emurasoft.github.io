# Editor\_DocInfoEx

检索或设置用于 EmEditor 的信息参数之一的值。你能直接用该内联函数或明确地发送
[EE\_INFO\_EX 消息](../message/ee_info_ex)。

Editor\_DocInfoEx( HWND hwnd, int iDoc, int nCmd, LPARAM lParam );

## 参数

_nCmd_

> 指定要检索或设置的参数。命令条目请参考 [EE\_INFO](../message/ee_info) 消息。

_hDoc_

> 指定目标文档的句柄。如果指定 NULL，则当前的活动文档将成为目标。根据 nCmd，也有可能不使用此参数。

_lParam_

> 取决于指定的参数。

## 返回值

> 取决于指定的参数。

## 支持版本

> 支持 EmEditor Professional v21.8 或之后的版本。
