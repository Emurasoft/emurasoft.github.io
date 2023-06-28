# COLUMN\_STRUCT

用于 [Editor\_SetColumn](../macro/editor_setcolumn)
内联函数 ( [EE\_SET\_COLUMN](../message/ee_set_column) 消息) 中。

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

## 字段

_cbSize_

> 指定此结构的大小 (以字节为单位)，sizeof(COLUMN\_STRUCT)。

_iColumn_

> 指定列的索引。

_yLineTop_

> 指定要设置的第一行的行号。

_yLines_

> 限制要设置的行数。如果为零，则不指定限制。

_pBuf_

> 指定要设置或插入的字符串。字符串可以用在 strDelimiter 中指定的分隔符分隔开。

_cchBuf_

> 不使用。

_pszDelimiter_

> 指定用于 _pBuf_ 中分隔字符串的分隔符。如果空着或省略该参数，同样的字符串会用于列中的每一个单元格上。

_flags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | AUTO\_QUOTE | 检查字符串是否包含分隔符，换行符或引号，并在必要时跳过这些字符并添加引号。 |
> | DONT\_QUOTE | 不做上述过程。 |
> | ALWAYS\_QUOTE | 总是添加引号。 |