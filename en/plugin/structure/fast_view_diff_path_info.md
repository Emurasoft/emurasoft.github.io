# FAST\_VIEW\_DIFF\_PATH\_INFO

Used by
[EE\_INFO message](../message/ee_info) with EI\_GET\_FAST\_VIEW\_DIFF\_PATH.

```
typedef struct _FAST_VIEW_DIFF_PATH_INFO {
	UINT cbSize;
	LPCWSTR pszFile;
	size_t cchBuf;
	LPWSTR pBuf;
} FAST_VIEW_DIFF_PATH_INFO;
```

## Fields

_cbSize_

Specifies sizeof( FAST\_VIEW\_DIFF\_PATH\_INFO ).

_pszFile_

Specifies the path of the file.

_cchBuf_

Specifies the size of the buffer in characters including the terminating NULL.

_pBuf_

Specifies the pointer to the buffer to retrieve the path of the diff file. The path is not copied if this is NULL or if the buffer is too small. To get the required size, call the message with _pBuf_ set to NULL, and add 1 to the return value.

## Version

Supported on Version 26.4 or later.
