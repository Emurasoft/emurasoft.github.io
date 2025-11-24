# TEMP\_INFO

用於 [EE\_EDIT\_TEMP](../message/ee_edit_temp) 消息以及 [EVENT\_TEMP\_SAVING 事件](../event/index) 中。

```
typedef struct _TEMP_INFO {
	size_t cbSize;
	LPCWSTR pszTempText;
	LPCWSTR pszTitle;
	LPCWSTR pszIconPath;
	LPCWSTR pszConfig;
	POINT_PTR ptInitialCaret;
	UINT nID;
	UINT nEncoding;
	UINT nFlags;
} TEMP_INFO;
```

## 構成

_cbSize_

用位元數表示該數據結構的大小。把這個構成部分設為 sizeof( TEMP\_INFO ) 在發送 [EE\_EDIT\_TEMP](../message/ee_edit_temp) 消息前。

_pszTempText_

指定要打開一個新文檔的記憶體中的臨時文字檔案。

_pszTitle_

指定新文檔的標題。

_pszIconPath_

指定您想要用作新文檔的圖示路徑以及檔案名。

_pszConfig_

指定新文檔應使用的組態名稱。

_ptInitialCaret_

指定初始游標位置。

_nID_

指定一個 ID 當您想要啟動或關閉臨時文字檔案時。

_nEncoding_

指定檔案的編碼。

_nFlags_

指定下列值之一。

|     |     |
| --- | --- |
| TEMP\_INFO\_OPEN | 打開一個臨時文字檔案如果 nID 為零。啟動已存在的臨時文字檔案如果 nID 不是零。 |
| TEMP\_INFO\_CLOSE | 關閉用 nID 指定的臨時文字檔案。 |
| TEMP\_INFO\_SAVE | 儲存用 nID 指定的臨時文字檔案。 |
| TEMP\_INFO\_QUIT | 關閉由 nID 指定的臨時文字檔案而不儲存。 |
| TEMP\_INFO\_NO\_ID | 打開一個臨時文字檔案，不設定 ID。使用此旗標打開的文檔可以在使用者選擇 **「檔案」** 功能表中的 **「另存新檔」** 時儲存到檔案中。 |

## 支持版本

支持 EmEditor ９.00 或之後的版本.
