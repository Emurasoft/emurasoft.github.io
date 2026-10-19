# FAST\_VIEW\_DIFF\_PATH\_INFO

與 EI\_GET\_FAST\_VIEW\_DIFF\_PATH 一起用於 [EE\_INFO 消息](../message/ee_info)。

```
typedef struct _FAST_VIEW_DIFF_PATH_INFO {
	UINT cbSize;
	LPCWSTR pszFile;
	size_t cchBuf;
	LPWSTR pBuf;
} FAST_VIEW_DIFF_PATH_INFO;
```

## 欄位

_cbSize_

指定 sizeof( FAST\_VIEW\_DIFF\_PATH\_INFO )。

_pszFile_

指定檔案的路徑。

_cchBuf_

指定以字元為單位的緩衝區大小，包括終止空字元。

_pBuf_

指定一個指針指向用來檢索差異檔路徑的緩衝區。如果此值為 NULL 或緩衝區太小，則不會複製路徑。若要取得所需的大小，請將 _pBuf_ 設為 NULL 來呼叫此消息，然後將返回值加 1。

## 版本

支持 Version 26.4 或之後的版本。
