# Editor\_DocInfo

检索或设置用于 EmEditor 的信息参数之一的值。你能直接用该内联函数或明确地发送
[EE\_INFO](../message/ee_info) 消息。

Editor\_DocInfo( HWND hwnd, int iDoc, int nCmd, LPARAM lParam );

## 参数

_nCmd_

> 指定要检索或设置的参数。命令条目请参考 [EE\_INFO](../message/ee_info) 消息。

_iDoc_

> 指定从零开始的目标文档的索引。如果指定值为 -1，则当前活动文档将被设为目标文档。

_lParam_

> 取决于指定的参数。

## 返回值

> 取决于指定的参数。

## 支持版本

> 支持 EmEditor 5.00 或之后的版本。
