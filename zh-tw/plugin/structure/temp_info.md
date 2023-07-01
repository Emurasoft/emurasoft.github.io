# TEMP\_INFO

用於 [EE\_EDIT\_TEMP](../message/ee_edit_temp) 消息以及 [EVENT\_TEMP\_SAVING 事件](../event/index) 中。

typedef struct \_TEMP\_INFO {

size\_t cbSize;

LPCWSTR pszTempText;

LPCWSTR pszTitle;

LPCWSTR pszIconPath;

LPCWSTR pszConfig;

POINT\_PTR ptInitialCaret;

UINT nID;

UINT nEncoding;

UINT nFlags;

} TEMP\_INFO;

## 構成

_cbSize_

> 用位元數表示該數據結構的大小。把這個構成部分設為 sizeof( TEMP\_INFO ) 在發送 [EE\_EDIT\_TEMP](../message/ee_edit_temp) 消息前。

_pszTempText_

> 指定要打開一個新文檔的內存中的臨時文本。

_pszTitle_

> 指定新文檔的標題。

_pszIconPath_

> 指定您想要用作新文檔的圖示路徑以及檔案名。

_pszConfig_

> 指定新文檔應使用的配置名稱。

_ptInitialCaret_

> 指定初始光標位置。

_nID_

> 指定一個 ID 當您想要激活或關閉臨時文本時。

_nEncoding_

> 指定檔案的編碼。

_nFlags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | TEMP\_INFO\_OPEN | 打開臨時文本如果 nID 為零。激活已存在的臨時文本如果 nID 不是零。 |
> | TEMP\_INFO\_CLOSE | 關閉用 nID 指定的臨時文本。 |
> | TEMP\_INFO\_SAVE | 保存用 nID 指定的臨時文本。 |

## 支持版本

> 支持 EmEditor ９.00 或之後的版本.
