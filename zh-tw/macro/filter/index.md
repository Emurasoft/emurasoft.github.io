# Filter 對象

## 屬性

|     |     |
| --- | --- |
| [Enabled](enabled) | 指定表示對象是否啟用的標志。 |
| [Value](value) | 指定要搜索的字串。 |
| [Column](column) | 指定你想要搜索的以 1 為基準的文字的欄的索引。指定 0 如果你想要搜索整行，或指定 -1 如果你想要把文字的開始字元和結尾字元作為 _Begin_ 和 _End_ 屬性。 |
| [Flags](flags) | 指定標志的組合。 |
| [Begin](begin) | 指定你要搜索的文字的起始欄的索引 (邏輯字元數)。指定 0 如果你想要把文字的最后一部分指定為 _End_。要啟用這個欄位， _Column_ 屬性必須是 -1 。 |
| [End](end) | 指定你要搜索的文字的末尾欄的索引 (邏輯字元數)。指定 0 如果你想要搜索剩余的文字。要啟用這個欄位， _Column_ 屬性必須是 -1 。 |
| [ExFlags](exflags) | 指定標志的組合。 |
| [Replace](replace) | 指定要取代為的字串。 |

## 版本

支持 EmEditor Professional Version 16.0 或之後的版本。


```{toctree}
:hidden:
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
