# COMPARE\_INFO

用于 [EE\_COMPARE](../message/ee_compare) 消息。

typedef struct \_COMPARE\_INFO {

UINT cbSize;

UINT flags;

LPCWSTR pszDocument1;

LPCWSTR pszDocument2;

LPCWSTR pszResultFileName;

} COMPARE\_INFO;

## 字段

_cbSize_

> 指定结构的大小，sizeof( COMPARE\_INFO )。

_flags_

> 指定以下值的组合。
>
> |     |     |
> | --- | --- |
> | COMPARE\_GENERATE\_REPORT | 生成一个报告文件。必须在 strResultFileName 中指定路径名称。 |
> | COMPARE\_IGNORE\_CASE | 忽略大小写。 |
> | COMPARE\_IGNORE\_COMMENT | 忽略配置标记为注释的文本。 |
> | COMPARE\_IGNORE\_CRLF | 忽略换行符的差异。 |
> | COMPARE\_IGNORE\_EMBEDDED\_SPACE | 忽略一行中第一个和最后一个非空格字符之间的空格。 |
> | COMPARE\_IGNORE\_ENCODING | 忽略编码差异。 |
> | COMPARE\_IGNORE\_LEAD\_SPACE | 忽略一行中第一个非空格字符之前的空格。 |
> | COMPARE\_IGNORE\_TRAIL\_SPACE | 忽略一行中最后一个非空格字符后的空格。 |
> | COMPARE\_OPEN\_REPORT | 打开报告文件。必须指定 COMPARE\_GENERATE\_REPORT。 |
> | COMPARE\_REPORT\_3\_COL | 使用 3 列格式输出报告。 |
> | COMPARE\_REPORT\_DIFF\_ONLY | 仅报告不相同的行。 |
> | COMPARE\_QUALITY\_1 | 搜索附近行的最快的方法。 |
> | COMPARE\_QUALITY\_2 | 较快的方法。 |
> | COMPARE\_QUALITY\_3 | 中等速度。 |
> | COMPARE\_QUALITY\_4 | 较精确的方法。 |
> | COMPARE\_QUALITY\_5 | 搜索整个文件最精确的方法（有一定的限制）。 |
> | COMPARE\_QUICK | 快速比较，不会突出显示差异。此标志不能与除 COMPARE\_QUIET 之外的其他选项结合使用。 |
> | COMPARE\_QUIET | 不显示任何输出消息。 |
> | COMPARE\_RESET | 重置比较或同步滚动模式并清除比较结果。 |
> | COMPARE\_RESET\_AFTER | 重置比较或同步滚动模式并在比较和报告生成后清除比较结果。另外，必须被指定 COMPARE\_GENERATE\_REPORT。 |
> | COMPARE\_RESTORE\_POS | 完成后恢复窗口位置。 |
> | COMPARE\_SPLIT\_VERT | 垂直分割窗口以显示文档。 |
> | COMPARE\_SWITCH\_NO\_WRAP | 切换到不换行。 |
> | COMPARE\_SYNC\_CARET | 同步光标位置。 |
> | COMPARE\_SYNC\_SCROLL\_HORZ | 同步水平滚动。 |
> | COMPARE\_SYNC\_SCROLL\_ONLY | 显示比较文档但不用高亮显示差异。 |
> | COMPARE\_SYNC\_SCROLL\_VERT | 同步垂直滚动。 |
> | COMPARE\_TILE\_HORZ | 水平平铺文件。 |
> | COMPARE\_TILE\_VERT | 垂直平铺文件。 |

_pszDocument1_

> 指定用于标识第一个文档的字符串。该值可以是文件名，带完整路径的文件名或一个冒号 (:) 后跟当前组中的文档索引。例如，"filename.csv"，"C:\\data\\filename.csv"，或 ":2"。

_pszDocument2_

> 指定用于标识第二个文档的字符串。该值的格式与 strDocument1 相同。

_pszResultFileName_

> 如果在 flags 字段指定了 COMPARE\_GENERATE\_REPORT，EmEditor 会用指定的文件名保存比较报告。

## 版本

> 支持 EmEditor Professional v17.7 或之后的版本。