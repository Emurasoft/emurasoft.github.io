# Editor\_GetUnicodeName

检索指定字符或字符串的 Unicode 名。你能直接用该内联函数或明确地发送 [EE\_GET\_UNICODE\_NAME](../message/ee_get_unicode_name) 消息。

int Editor\_GetUnicodeName( HWND hwnd, LPWSTR pBuf, int cchBuf, LPCWSTR pstrSrc, int cchSrc );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pBuf_

指定指针指向的能检索 Unicode 名的缓冲区。

_cchBuf_

以字节为单位指定缓冲区大小，包括终止空字符。

_pstrSrc_

指定源字符或字符串。

_cchSrc_

指定在 _pstrSrc_ 中指定的字符数。

## 返回值

如果 UNICODE\_NAME\_INFO 结构的 _cchBuf_ 字段是零，那返回值则是用字符数表示的一个会接收文本的缓冲区的必需大小。

## 版本

支持 EmEditor Professional 19.1 或之后的版本。
