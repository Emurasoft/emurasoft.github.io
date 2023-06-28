# Editor\_EnumConfig

列举可用的配置。你能直接用该内联函数或明确地发送 [EE\_ENUM\_CONFIG](../message/ee_enum_config) 消息。

Editor\_EnumConfig( HWND hwnd, LPWSTR pBuf, size\_t cchBuf );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_cchBuf_

> 用字符数指定缓冲区大小。要注意的是两个空字符会被添加到配置列表末尾。如果指定的数值为 0，该消息会返回检索配置列表的必需大小。

_pBuf_

> 指定指针指向缓冲区来检索配置列表。在这个缓冲区内，由一个空字符分隔的可用的配置列表会被检索。两个空字符会被添加到配置列表末尾。如果指定的数值为 0，pBuf 是空 (NULL)。

## 返回值

> 返回值是检索配置列表的必需大小。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。