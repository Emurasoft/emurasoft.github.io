# FAST\_VIEW\_DIFF\_PATH\_INFO

与 EI\_GET\_FAST\_VIEW\_DIFF\_PATH 一起用于
[EE\_INFO 消息](../message/ee_info)。

```
typedef struct _FAST_VIEW_DIFF_PATH_INFO {
	UINT cbSize;
	LPCWSTR pszFile;
	size_t cchBuf;
	LPWSTR pBuf;
} FAST_VIEW_DIFF_PATH_INFO;
```

## 字段

_cbSize_

指定 sizeof( FAST\_VIEW\_DIFF\_PATH\_INFO )。

_pszFile_

指定文件的路径。

_cchBuf_

以字符为单位指定缓冲区的大小，包括终止 NULL 字符。

_pBuf_

指定用于检索差异文件路径的缓冲区的指针。如果此值为 NULL 或缓冲区太小，则不会复制路径。要获取所需的大小，请在 _pBuf_ 设为 NULL 的情况下调用该消息，然后将返回值加 1。

## 版本

支持 26.4 或更高版本。
