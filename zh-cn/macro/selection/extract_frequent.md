# ExtractFrequent 方法 (Selection ����)

将常用字符串提取到新文档中。

## 

### \[JavaScript\]

```
document.selection.ExtractFrequent( nType, nFlags, nCsvFormat, nNumOfLines, sIgnore );
```

### \[VBScript\]

```
document.selection.ExtractFrequent nType, nFlags, nCsvFormat, nNumOfLines, sIgnore
```

## 参数

_nType_

指定下列值之一。如果省略，则使用 eeFreqTypeLines。

| 值 | 含义 |
| --- | --- |
| eeFreqTypeLines | 创建一个常用行列表。 |
| eeFreqTypeWords | 创建一个常用词列表。单词是由非字母数字字符包围的字符串，可以通过在自定义 对话框中的 [编辑 页面](../../dlg/customize/edit/index) 上的将下列字符识别为字母数字 文本框来自定义。 |
| eeFreqTypeCells | 创建一个常用单元格列表。 |
| eeFreqTypeIPv4 | 创建一个常用 IPv4 地址列表。 |
| eeFreqTypeIPv6 | 创建一个常用 IPv6 地址列表。 |

_nNumOfLines_

指定要提取的最大字符串数。实际输出可能会超过此数字，以便包括所有同一频率检测到的多个字符串。如果省略，则使用默认值。

_iCsvFormat_

指定要显示的 CSV 格式。如果省略，则使用第一个定义的 CSV 格式。

_nFlags_

指定以下值的组合。如果省略，则使用 0。

| 值 | 含义 |
| --- | --- |
| eeFindReplaceCase | 大小写需符合。 |
| eeFindReplaceOpenDoc | 在同一个框架窗口中，搜索所有打开的文档。 |
| eeFindReplaceSelOnly | 仅在选区内搜索。 |

_pszIgnore_

指定在计算常用字符串时要忽略的字符串。多个字符串必须用换行符 (\\n) 分隔。如果省略，则使用空字符串。

## 版本

支持 EmEditor Professional Version 21.9 或之后的版本。
