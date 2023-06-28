# Editor\_DocGetModified

检索指定文档的文本的修改状态。你能直接用该内联函数或明确地发送 [EE\_GET\_MODIFIED](../message/ee_get_modified) 消息。

Editor\_DocGetModified( HWND hwnd, int iDoc );

Editor\_DocGetModified( HWND hwnd, HEEDOC hDoc );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_iDoc_

> 指定目标文档的索引。如果指定值为 -1，当前活动文档会被设为目标文档。

_hDoc_

> 指定目标文档的句柄。如果指定 NULL，则当前的活动文档将成为目标。

## 返回值

> 如果文本被修改，返回值是 TRUE。如果文本没有被修改，返回值是 FALSE。

## 支持版本

> 支持 EmEditor 5.00 或之后的版本。