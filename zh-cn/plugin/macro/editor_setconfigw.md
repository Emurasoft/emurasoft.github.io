# Editor\_SetConfigW

变更为一个用 Unicode 字符串指定的配置。你能直接用该内联函数或明确地发送 [EE\_SET\_CONFIGW](../message/ee_set_configw) 消息。

Editor\_SetConfigW( HWND hwnd, LPCWSTR szConfigName );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_szConfigName_

用 Unicode 字符串指定一个配置。

## 返回值

不使用返回值。
