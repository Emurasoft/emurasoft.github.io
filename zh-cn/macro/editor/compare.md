# Compare 方法 (Editor ����)

比较两个文档。

#### \[JavaScript\]

_n_ = editor. **Compare**( _nFlags_, _strDocument1_, _strDocument2_\[, _strResultFileName_\] );

#### \[VBScript\]

_n_ = editor. **Compare**( _nFlags_, _strDocument1_, _strDocument2_\[, _strResultFileName_\] )

## 参数

_nFlags_

你可以指定以下值的组合。

|     |     |
| --- | --- |
| eeCompareGenerateReport | 生成一个报告文件。必须在 strResultFileName 中指定路径名称。 |
| eeCompareOpenReport | 打开报告文件。必须指定 eeCompareGenerateReport。 |
| eeCompareQuality1 | 搜索附近行的最快的方法。 |
| eeCompareQuality2 | 较快的方法。 |
| eeCompareQuality3 | 中等速度。 |
| eeCompareQuality4 | 较精确的方法。 |
| eeCompareQuality5 | 搜索整个文件最精确的方法（有一定的限制）。 |
| eeCompareQuick | 快速比较，不会突出显示差异。此标志不能与除 eeCompareQuiet 之外的其他选项结合使用。 |
| eeCompareQuiet | 不显示任何输出消息。 |
| eeCompareReport3Col | 使用 3 列格式输出报告。 |
| eeCompareReportDiffOnly | 仅报告不相同的行。 |
| eeCompareReset | 重置比较或同步滚动模式并清除比较结果。 |
| eeCompareResetAfter | 重置比较或同步滚动模式并在比较和报告生成后清除比较结果。另外，必须被指定 eeCompareGenerateReport。 |
| eeCompareRestorePos | 完成后恢复窗口位置。 |
| eeCompareSplitVert | 垂直分割窗口以显示文档。 |
| eeCompareSwitchNoWrap | 切换到不换行。 |
| eeCompareSyncCaret | 同步光标位置。 |
| eeCompareSyncScrollHorz | 同步水平滚动。 |
| eeCompareSyncScrollOnly | 显示比较文档但不用高亮显示差异。 |
| eeCompareSyncScrollVert | 同步垂直滚动。 |
| eeCompareTileHorz | 水平平铺文件。 |
| eeCompareTileVert | 垂直平铺文件。 |
| eeIgnoreCases | 忽略大小写。 |
| eeIgnoreComments | 忽略配置标记为注释的文本。 |
| eeIgnoreEmbeddedSpaces | 忽略一行中第一个和最后一个非空格字符之间的空格。 |
| eeIgnoreEncodings | 忽略编码差异。 |
| eeIgnoreLeadSpaces | 忽略一行中第一个非空格字符之前的空格。 |
| eeIgnoreNewlines | 忽略换行符的差异。 |
| eeIgnoreTrailingSpaces | 忽略一行中最后一个非空格字符后的空格。 |

_strDocument1_

指定用于标识第一个文档的字符串。该值可以是文件名，带完整路径的文件名或一个冒号 (:) 后跟当前组中的文档索引。 例如，"filename.csv"，"C:\\data\\filename.csv" (在 JavaScript 中是"C:\\\data\\\filename.csv")，或 ":2"。

_strDocument2_

指定用于标识第二个文档的字符串。该值的格式与 strDocument1 相同。

_strResultFileName_

如果指定了此参数和 eeCompareGenerateReport，EmEditor 会保存比较报告到此路径，包括名称。

## 返回值

返回值是以下值之一。

|     |     |
| --- | --- |
| eeDiff | 两个文档不相同。 |
| eeMatched | 两个文档相同。 |
| eeMatchedIgnored | 除了被忽略的地方外，两个文档是相同的。 |

## 版本

支持 EmEditor Professional v17.7 或之后的版本。