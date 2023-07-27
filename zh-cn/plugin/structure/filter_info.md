# FILTER\_INFO

用于 [EE\_FILTER](../message/ee_filter) 消息。

typedef struct \_FILTER\_INFO {

UINT     cchSize;

UINT     flags;

int      iColumn;

LPCWSTR  pszFilter;

INT\_PTR  xBegin;

INT\_PTR  xEnd;

} FILTER\_INFO;

## 字段

_cch_

指定这个结构的大小，sizeof( FILTER\_INFO )。

_flags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 大小写需符合。 |
| FLAG\_FIND\_CONTINUE | 指定下次调用的 EE\_FILTER 消息不会清除筛选记录。在调用这个消息之后，这个筛选不会被马上应用。你可以在你要进行多个级别的筛选时，使用这个标志。它与 FLAG\_FIND\_KEEP\_PREVIOUS 标志相同，但由于实际的筛选不会在每次调用消息时被应用，这个方法更适用于多个筛选级别。 |
| FLAG\_FIND\_ESCAPE | 使用转义序列。 |
| FLAG\_FIND\_KEEP\_PREVIOUS | 指定 EE\_FILTER 消息不会在应用新筛选前清除已存在的筛选记录。你可以在你要进行多个级别的筛选时，使用这个标志。 |
| FLAG\_FIND\_LOGICAL\_OR | 指定一个逻辑或运算 (logical OR) 到之前的层级上在多层级筛选的情况下。 |
| FLAG\_FIND\_NEGATIVE | 显示筛选工具栏并排除与指定字符串匹配的行。 |
| FLAG\_FIND\_ONLY\_WORD | 整个单词需匹配。 |
| FLAG\_FIND\_REG\_EXP | 使用一个正则表达式。 |
| FLAG\_FIND\_REMOVE\_LAST | 删除前一次添加的筛选级别。 |

_iColumn_

指定你想要搜索的文本的列索引，或指定 -1 如果你想要搜索整行。如果你要用字符数把开始以及结束的文本指定为 _xBegin_ 和 _xEnd_，可以指定 -2。

_pszFilter_

指定一个要搜索的字符串。

_xBegin_

指定你想要搜索的文本的列开始的索引（用逻辑字符数）；你也可以指定 -1 如果你想要把文本的最后一部分作为 _xEnd_。要使这个字段有效， _iColumn_ 值必须是 -2。

_xEnd_

指定你想要搜索的文本的列结束的索引（用逻辑字符数）；你也可以指定 -1 如果你想要搜索所有剩下的文本。要使这个字段有效， _iColumn_ 值必须是 -2。

## 版本

支持 EmEditor Professional 14.7 或之后的版本。
