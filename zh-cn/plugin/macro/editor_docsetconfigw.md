# Editor\_DocSetConfigW

把指定文档变更为一个用 Unicode 字符串指定的配置。你能直接用该内联函数或明确地发送 [EE\_SET\_CONFIGW](../message/ee_set_configw) 消息。

Editor\_SetConfigW( HWND hwnd, int iDoc, LPCWSTR szConfigName );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_iDoc_

> 指定目标文档的索引。如果指定值为 -1，当前活动文档会被设为目标文档。

_szConfigName_

> 用 Unicode 字符串指定一个配置。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 5.00 或之后的版本。
