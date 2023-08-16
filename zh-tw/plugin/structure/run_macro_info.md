# RUN\_MACRO\_INFO

用於 [EE\_RUN\_MACRO](../message/ee_run_macro) 消息。

```
typedef struct _RUN_MACRO_INFO {
	size_t cbSize;
	LPCWSTR pszMacroFile;
	LPCWSTR pszText;
	UINT nFlags;
	int nDefMacroLang;
	POINT_PTR ptOrgPos;
	POINT_PTR ptCodePos;
	POINT_PTR ptErrorPos;
	HGLOBAL hstrResult;
} RUN_MACRO_INFO;
```

## 構成

_cbSize_

以位元為單位的數據結構大小。在發送 EE\_RUN\_MACRO 消息之前，把該成員設為 sizeof( RUN\_MACRO\_INFO )。

_pszMacroFile_

指定您想要運行的巨集檔案的路徑以及檔案名稱。

_pszText_

在內存上指定您想要運行的一段巨集文本。

_nFlags_

指定下列值之一。

|     |     |
| --- | --- |
| RUN\_FILE | pszMacroFile 參數有效。 |
| RUN\_TEXT | pszText 參數有效。 |

_nDefMacroLang_

指定下列值的組合。

|     |     |
| --- | --- |
| MACRO\_LANG\_JSCRIPT | 該巨集是 JScript。 |
| MACRO\_LANG\_V8 | 該巨集是 V8。 |
| MACRO\_LANG\_VBSCRIPT | 該巨集是 VBScript。 |
| MACRO\_LANG\_UNKNOWN | 該巨集語言未知。 |
| MACRO\_SYNC\_ONLY | 同步執行巨集。 |

_ptOrgPos_

指定巨集的原始位置。

_ptCodePos_

指定巨集的代碼位置。

_ptErrorPos_

接收巨集的錯誤位置。

_hstrResult_

輸出。接收句柄到巨集所返回的輸出字符串中。調用方負責使用 GlobalFree 函數來釋放該句柄。

## 支持版本

支持 EmEditor 9.00 或之後的版本。
