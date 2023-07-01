# Filter 对象

## 属性

|     |     |
| --- | --- |
| [Enabled](enabled) | 指定表示对象是否启用的标志。 |
| [Value](value) | 指定要搜索的字符串。 |
| [Column](column) | 指定你想要搜索的以 1 为基准的文本的列的索引。指定 0 如果你想要搜索整行，或指定 -1 如果你想要把文本的开始字符和结尾字符作为 _Begin_ 和 _End_ 属性。 |
| [Flags](flags) | 指定标志的组合。 |
| [Begin](begin) | 指定你要搜索的文本的起始列的索引 (逻辑字符数)。指定 0 如果你想要把文本的最后一部分指定为 _End_。要启用这个字段， _Column_ 属性必须是 -1 。 |
| [End](end) | 指定你要搜索的文本的末尾列的索引 (逻辑字符数)。指定 0 如果你想要搜索剩余的文本。要启用这个字段， _Column_ 属性必须是 -1 。 |
| [ExFlags](exflags) | 指定标志的组合。 |
| [Replace](replace) | 指定要替换为的字符串。 |

## 版本

支持 EmEditor Professional Version 16.0 或之后的版本。


```{toctree}
:maxdepth: 1
begin
column
enabled
end
exflags
flags
replace
value
```
