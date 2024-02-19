# Join 方法 (Editor 对象)

按指定键列，用一个与 JOIN 操作类似的方法合并两个 CSV 文档，并创建一个新文档。

## 

### \[JavaScript\]

```
n = editor.Join( nFlags, strDocument1, strColumn1, strDocument2, strColumn2, strSelect, strSeparator, nLimit );
```

### \[VBScript\]

```
n = editor.Join( nFlags, strDocument1, strColumn1, strDocument2, strColumn2, strSelect, strSeparator, nLimit)
```

## 参数

_nFlags_

你能指定一个下列值的组合。不能组合 eeJoinSimpleMerge，eeJoinContain，eeJoinStartWith，和 eeJoinEndWith。

|     |     |
| --- | --- |
| eeJoinUniqueKey1 | 在第一个文档中的指定列包含一个唯一键。 |
| eeJoinUniqueKey2 | 在第二个文档中的指定列包含一个唯一键。 |
| eeJoinIncludeAll1 | 第一个文档中的所有行都会被包括在输出中。输出文档将包含空的单元格如果第一个文档中的行没有匹配的结果。 |
| eeJoinIncludeAll2 | 第二个文档中的所有行都会被包括在输出中。输出文档将包含空的单元格如果第二个文档中的行没有匹配的结果。 |
| eeJoinMatchCase | 匹配大小写。 |
| eeJoinSimpleMerge | 不比较关键值，直接合并两个文档。如果指定该选项，那么 _strColumn1_ 和 _strColumn2_ 的参数会被忽略。 |
| eeJoinIgnoreHeadings1 | 忽略第一个文档中的标题，让第一个文档中的标题能在合并后的档案中保留。 |
| eeJoinIgnoreHeadings2 | 忽略第二个文档中的标题。 |
| eeJoinContain | Key1 包含 Key2。 |
| eeJoinStartWith | Key1 以 Key2 开始。 |
| eeJoinEndWith | Key1 以 Key2 结尾。 |
| eeJoinMatchSplitBoth | 两个拆分的字符串都匹配。 |
| eeJoinMatchSplitOne | Key1 匹配拆分的 Key2。 |
| eeJoinFuzzy | 使用模糊匹配。 此标志不能与 eeJoinEndWith、eeJoinMatchSplitBoth 或 eeJoinMatchSplitOne 结合使用。此标志会使过程变慢。 |
| eeJoinSwap | Key1 和 Key2 互换，如果还指定了 eeJoinContain，eeJoinStatWith，eeJoinEndWith，或 eeJoinMatchSplitOne。 |

_strDocument1_

指定字符串来识别第一个文档。这个值可以是文件名，文件名以及路径，或一个冒号 (:) 后跟当前群组中指定文档的索引号。例如，"filename.csv"，"C:\\data\\filename.csv" (如果是 JavaScript，"C:\\\\data\\\\filename.csv")，或 ":2"。

_strColumn1_

指定字符串来识别第一个文档的键列。这个值可以是指定列的第一行或一个冒号 (:) 后跟指定列的索引号。例如，"first\_name"，":5"，"1-5"，或 "2-"。

_strDocument2_

指定字符串来识别第二个文档。这个值的格式与 strDocument1 格式相同。

_strColumn2_

指定字符串来识别第二个文档的键列。这个值的格式与 strColumn1 格式相同。

_strSelect_

指定字符串来选择要包括在输出文档中的列。例如，"file1.csv>column1,file2.csv>column2"。

_strSeparator_

在拆分单元格时，将字符串指定为分隔符。除非指定 eeJoinMatchSplitBoth 或 eeJoinMatchSplitOne，否则将忽略此参数。

_nLimit_

指定每个单元格的最大拆分次数。如果省略或指定为 0，则该方法将不限制拆分次数。除非指定 eeJoinMatchSplitBoth 或 eeJoinMatchSplitOne，否则将忽略此参数。

## 返回值

返回值是与指定字符串匹配的行数。

## 版本

支持 EmEditor 14.8 或之后的版本。
