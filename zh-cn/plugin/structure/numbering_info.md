# NUMBERING\_INFO

用于 [EE\_NUMBERING 消息](../message/ee_numbering)。

```
typedef struct _NUMBERING_INFO {
	UINT cbSize;
	UINT nFlags;
	LPCWSTR pszFirst;
	LPCWSTR pszInc;
	INT64 nMaxLines;
} NUMBERING_INFO;
```

## 字段

_cbSize_

指定这个结构的大小，sizeof( NUMBERING\_INFO )。

_nFlags_

你可以指定以下值的组合。

| 值 | 含义 |
| --- | --- |
| NUM\_FLAG\_CAPITAL\_LETTERS | 以大写字母插入十六进制值。 |
| NUM\_FLAG\_SKIP\_EMPTY\_LINES | 在空行后继续编号，而不会在垂直选择模式或多选区模式期间对空行进行编号。 |
| NUM\_FLAG\_RESTART\_NUM\_EMPTY | 在垂直选择模式或多选区模式下，编号在空行后将从第一个值重新开始。 |
| NUM\_FLAG\_RESTART\_NUM\_DISCONTINUOUS | 在多选区模式下，编号将在不连续的行处从第一个值重新开始。 |
| NUM\_FLAG\_DECIMAL | 以十进制形式插入数字。 |
| NUM\_FLAG\_HEXADECIMAL | 以十六进制形式插入数字。 |
| NUM\_FLAG\_OCTAL | 以八进制形式插入数字。 |
| NUM\_FLAG\_BINARY | 以二进制形式插入数字。 |
| NUM\_FLAG\_OTHER | 插入字符而不是数字。从 _pszFirst_ 参数中指定的数字开始，此选项插入用在 _pszInc_ 参数中指定的 Unicode 值的增量的连续字符。每行只能插入一个字符。 |

_pszFirst_

指定要在第一行插入的初始值或字符。

_pszInc_

指定十进制形式的增量。这是第一行和第二行之间的值的变化。

_nMaxLines_

指定十进制形式的行数。

## 版本

支持 EmEditor Professional 19.1 或之后的版本。
