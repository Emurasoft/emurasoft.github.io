# Editor\_Join

按指定键列,用一个与 JOIN 操作类似的方法合并两个 CSV 文档,并创建一个新文档。你可以用该内联函数或直接发送 [EE\_JOIN](../message/ee_join) 消息。

Editor\_Join( HWND hwnd, UINT nFlags, LPCWSTR pszDocument1, LPCWSTR pszColumn1, LPCWSTR pszDocument2, LPCWSTR pszColumn2, LPCWSTR pszSelect, int\* piDocument3 );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nFlags_

> 你能指定下列值的一个组合。
>
> |     |     |
> | --- | --- |
> | JOIN\_FLAG\_UNIQUE\_KEY\_1 | 在第一个文档中的指定列包含一个唯一键。 |
> | JOIN\_FLAG\_UNIQUE\_KEY\_2 | 在第二个文档中的指定列包含一个唯一键。 |
> | JOIN\_FLAG\_INCLUDE\_ALL\_1 | 第一个文档中的所有行都会被包括在输出中。输出文档将包含空的单元格如果第一个文档中的行没有匹配的结果。 |
> | JOIN\_FLAG\_INCLUDE\_ALL\_2 | 第二个文档中的所有行都会被包括在输出中。输出文档将包含空的单元格如果第二个文档中的行没有匹配的结果。 |
> | JOIN\_FLAG\_MATCH\_CASE | 匹配大小写。 |
> | JOIN\_FLAG\_SIMPLE\_JOIN | 合并两个文档而不比较键。如果指定了此标志，则会忽略 _pszColumn1_ 和 _pszColumn2_ 参数。 |
> | JOIN\_FLAG\_IGNORE\_HEADINGS\_1 | 忽略第一个文档中的标题，以便将第一个文档中的标题保留在合并的文档中。 |
> | JOIN\_FLAG\_IGNORE\_HEADINGS\_2 | 忽略第二个文档中的标题。 |
> | JOIN\_FLAG\_CONTAIN | Key1 包含 Key2。 |
> | JOIN\_FLAG\_START\_WITH | Key1 以 Key2 开始。 |
> | JOIN\_FLAG\_END\_WITH | Key1 以 Key2 结尾。 |
> | JOIN\_FLAG\_MATCH\_SPLIT\_BOTH | 两个拆分的字符串都匹配。 |
> | JOIN\_FLAG\_MATCH\_SPLIT\_ONE | Key1 匹配拆分的 Key2。 |
> | JOIN\_FLAG\_FUZZY | 使用模糊匹配。 此标志不能与 JOIN\_FLAG\_END\_WITH、JOIN\_FLAG\_MATCH\_SPLIT\_BOTH 或 JOIN\_FLAG\_MATCH\_SPLIT\_ONE 结合使用。此标志会使过程变慢。 |
> | JOIN\_FLAG\_SWAP | Key1 和 Key2 互换，如果还指定了 JOIN\_FLAG\_CONTAIN，JOIN\_FLAG\_START\_WITH，或 JOIN\_FLAG\_END\_WITH。 |

_pszDocument1_

> 指定字符串来识别第一个文档。这个值可以是文件名，文件名以及路径，或一个冒号 (:) 后跟当前群组中指定文档的索引号。例如，"filename.csv"，"C:\\data\\filename.csv" (如果是 JavaScript，"C:\\\data\\\filename.csv")，或 ":2"。

_pszColumn1_

> 指定字符串来识别第一个文档的键列。这个值可以是列的第一行或一个冒号 (:) 后跟指定列的索引号。例如，"first\_name" 或 ":5"。

_pszDocument2_

> 指定字符串来识别第二个文档。这个值的格式与 pszDocument1 格式相同。

_pszColumn2_

> 指定字符串来识别第二个文档的键列。这个值的格式与 pszColumn1 格式相同。

_pszSelect_

> 指定字符串来选择要包括在输出文档中的列。例如，"file1.csv>column1,file2.csv>column2"。

_piDocument3_

> 这个字段将充满输出文档的索引，当函数返回时。如果这个值为 NULL，这个字段会被忽略。

## 返回值

> 返回值是新文档的行数。返回值为负数如果发生错误的话。如果发生错误,返回值是下列值之一:
>
> |     |     |
> | --- | --- |
> | E\_DOCUMENT\_1\_NOT\_FOUND | 无法找到第一个文档。 |
> | E\_DOCUMENT\_2\_NOT\_FOUND | 无法找到第二个文档。 |
> | E\_COLUMN\_1\_NOT\_FOUND | 无法找到第一列。 |
> | E\_COLUMN\_2\_NOT\_FOUND | 无法找到第二列。 |
> | E\_SELECT\_SYNTAX | 选择的字符串中有语法错误。 |
> | E\_SELECT\_DOCUMENT\_NOT\_FOUND | 无法在选择的字符串中找到指定的文档。 |
> | E\_SELECT\_COLUMN\_NOT\_FOUND | 无法在选择的字符串中找到指定列。 |
> | E\_DIFFERENT\_CSV\_MODE | 不同的 CSV 模式。 |
> | E\_NOT\_MDI | 必须启用 Tab。 |
> | E\_WRITE\_TEMP\_FILE | 临时文件写入错误。 |
> | E\_ABORT | 被用户中止。 |
> | E\_FAIL | 未指定的错误。 |

## 版本

> 支持 EmEditor 14.8 或之后的版本。