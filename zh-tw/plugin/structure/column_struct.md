# COLUMN\_STRUCT

用於 [Editor\_SetColumn](../macro/editor_setcolumn)
內嵌函式 ( [EE\_SET\_COLUMN](../message/ee_set_column) 消息) 中。

typedef struct \_COLUMN\_STRUCT {

UINT cbSize;

int iColumn;

UINT\_PTR yLineTop;

UINT\_PTR yLines;

LPWSTR pBuf

UINT\_PTR cchBuf;

LPCWSTR pszDelimiter;

UINT flags;

HGLOBAL hGlobalData;

} COLUMN\_STRUCT;

## 欄位

_cbSize_

> 指定此結構的大小 (以字節為單位)，sizeof(COLUMN\_STRUCT)。

_iColumn_

> 指定列的索引。

_yLineTop_

> 指定要設置的第一行的行號。

_yLines_

> 限制要設置的行數。如果為零，則不指定限制。

_pBuf_

> 指定要設置或插入的字串。字串可以用在 strDelimiter 中指定的分隔符分隔開。

_cchBuf_

> 不使用。

_pszDelimiter_

> 指定用於 _pBuf_ 中分隔字串的分隔符。如果空著或省略該參數，同樣的字串會用於列中的每一個儲存格上。

_flags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | AUTO\_QUOTE | 檢查字串是否包含分隔符，換行符或引號，并在必要時跳過這些字元并添加引號。 |
> | DONT\_QUOTE | 不做上述過程。 |
> | ALWAYS\_QUOTE | 總是添加引號。 |
