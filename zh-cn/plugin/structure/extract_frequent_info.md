# EXTRACT\_FREQUENT\_INFO

用于 [EE\_EXTRACT\_FREQUENT](../message/ee_extract_frequent) 消息。

typedef struct \_EXTRACT\_FREQUENT\_INFO {

UINT cbSize;

UINT nType;

UINT nNumOfLines;

UINT iCsvFormat;

UINT64 nFlags;

LPCWSTR pszIgnore;

} EXTRACT\_FREQUENT\_INFO;

## 字段

_cbSize_

> 指定 sizeof( EXTRACT\_FREQUENT\_INFO )。

_nType_

> 指定下列值之一。

> | 值 | 含义 |
> | --- | --- |
> | FREQ\_TYPE\_LINES | 创建一个常用行列表。 |
> | FREQ\_TYPE\_WORDS | 创建一个常用词列表。单词是由非字母数字字符包围的字符串，可以通过在 **自定义** 对话框中的 [**编辑** 页面](../../dlg/customize/edit/index) 上的 **将下列字符识别为字母数字** 文本框来自定义。 |
> | FREQ\_TYPE\_CELLS | 创建一个常用单元格列表。 |
> | FREQ\_TYPE\_IPV4 | 创建一个常用 IPv4 地址列表。 |
> | FREQ\_TYPE\_IPV6 | 创建一个常用 IPv6 地址列表。 |

_nNumOfLines_

> 指定要提取的最大字符串数。实际输出可能会超过此数字，以便包括所有同一频率检测到的多个字符串。

_iCsvFormat_

> 指定要显示的 CSV 格式。

_nFlags_

> 指定以下值的组合。
>
> | 值 | 含义 |
> | --- | --- |
> | FLAG\_FIND\_CASE | 大小写需符合。 |
> | FLAG\_FIND\_OPEN\_DOC | 在同一个框架窗口中，搜索所有打开的文档。 |
> | FLAG\_FIND\_SEL\_ONLY | 仅在选区内搜索。 |

_pszIgnore_

> 指定在计算常用字符串时要忽略的字符串。多个字符串必须用换行符 (\\n) 分隔。

## 版本

> 支持 EmEditor Professional 21.9 或之后的版本。
