# FAST\_VIEW\_DIFF\_PATH\_INFO

EI\_GET\_FAST\_VIEW\_DIFF\_PATH を指定した [EE\_INFO メッセージ](../message/ee_info)で使用します。

```
typedef struct _FAST_VIEW_DIFF_PATH_INFO {
	UINT cbSize;
	LPCWSTR pszFile;
	size_t cchBuf;
	LPWSTR pBuf;
} FAST_VIEW_DIFF_PATH_INFO;
```

## フィールド

_cbSize_

この構造体のサイズ、sizeof( FAST\_VIEW\_DIFF\_PATH\_INFO ) を指定します。

_pszFile_

ファイルのパスを指定します。

_cchBuf_

終端の NULL を含む、バッファのサイズを文字数で指定します。

_pBuf_

差分ファイルのパスを取得するバッファへのポインタを指定します。これが NULL の場合、またはバッファが小さすぎる場合は、パスはコピーされません。必要なサイズを取得するには、_pBuf_ を NULL に設定してメッセージを呼び出し、戻り値に 1 を加えます。

## バージョン

Version 26.4 以上で利用できます。
