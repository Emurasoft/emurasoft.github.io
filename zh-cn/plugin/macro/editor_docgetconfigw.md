# Editor\_DocGetConfigW

为指定的文档检索选取的配置名称并把它作为一个 Unicode 字符串。你能直接用该内联函数或明确地发送 [EE\_GET\_CONFIGW](../message/ee_get_configw) 消息。

Editor\_DocGetConfigW( HWND hwnd, int iDoc, LPWSTR szConfigName );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_iDoc_

> 指定目标文档的索引。如果指定值为 -1，当前活动文档会被设为目标文档。

_szConfigName_

> 指定会接收配置名称的一个缓冲区。缓冲区大小必须至少是MAX\_CONFIG\_NAME 字节。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 5.00 或之后的版本。
