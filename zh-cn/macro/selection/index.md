# Selection 对象

## 属性

|     |     |
| --- | --- |
|[Average](average) | 检索所选内容中包含的数字的平均值。 |
|[Count](selection_count) | 检索在当前文档中所选取的数目。 |
|[IsActiveEndGreater](selection_isactiveendgreater) | 表示活动点是否与底部点相同。 |
|[IsEmpty](selection_isempty) | 表示活动点是否与锚点相同。 |
|[Mode](selection_mode) | 设置或检索表示选取模式的标志。 |
|[OverwriteMode](selection_overwritemode) | 设置或检索表示改写或插入模式的标志。 |
|[Sum](sum) | 检索选择中包含的数字的总和。 |
|[Text](selection_text) | 检索被选取的文本，或在光标位置处插入一个字符串。 |

## 方法

|     |     |
| --- | --- |
|[BatchFind](batch_find) | 搜索多个字符串。 |
|[BatchReplace](batch_replace) | 替换多个字符串。 |
|[ChangeCase](selection_changecase) | 变更所选取的文本的大小写。 |
|[ChangeWidth](selection_changewidth) | 变更所选取的文本的宽度。 |
|[CharLeft](selection_charleft) | 把光标向左移动指定的字符数。 |
|[CharRight](selection_charright) | 把光标向右移动指定的字符数。 |
|[ClearBookmark](selection_clearbookmark) | 清除当前行上的书签。 |
|[Collapse](selection_collapse) | 折叠所选的部分到活动点。 |
|[Copy](selection_copy) | 复制选定内容到剪贴板上。 |
|[CopyLink](selection_copylink) | 复制光标处的超链接到剪贴板上。 |
|[Cut](selection_cut) | 把选取的文本移动到剪贴板上。 |
|[Delete](selection_delete) | 删除所选内容。 |
|[DeleteLeft](selection_deleteleft) | 删除所选内容或光标左边的指定字符数。 |
|[DestructiveInsert](selection_destructiveinsert) | 插入文本，覆盖已存在的文本。 |
|[DuplicateLine](selection_duplicateline) | 复制当前行。 |
|[EndOfDocument](selection_endofdocument) | 把光标移到文档末尾。 |
|[EndOfLine](selection_endofline) | 把光标移到当前行的尾端。 |
| [ExtractFrequent](extract_frequent) | 将常用字符串提取到新文档中。 |
|[Find](selection_find) | 搜索指定的字符串。 |
|[FindRepeat](selection_findrepeat) | 对同一个字符串重复上一次搜索。 |
|[Format](selection_format) | 插入或删除选定内容中的新行。 |
|[GetActivePointX](selection_getactivepointx) | 返回光标位置处的列号。 |
|[GetActivePointY](selection_getactivepointy) | 返回光标位置处的行号。 |
|[GetAnchorPointX](selection_getanchorpointx) | 返回选定内容原点的列号。 |
|[GetAnchorPointY](selection_getanchorpointy) | 返回选定内容原点的行号。 |
|[GetBottomPointX](selection_getbottompointx) | 返回选定内容底部的列号。 |
|[GetBottomPointY](selection_getbottompointy) | 返回选定内容底部的行号。 |
|[GetTopPointX](selection_gettoppointx) | 返回选定内容顶部的列号。 |
|[GetTopPointY](selection_gettoppointy) | 返回选定内容顶部的行号。 |
|[GoToBrace](selection_gotobrace) | 把光标移动到相对应的括号处。 |
|[Indent](selection_indent) | 按指定的缩进等级数来缩进被选取的行。 |
|[InsertDate](selection_insertdate) | 插入当前时间和日期。 |
|[InsertFromFile](selection_insertfromfile) | 在光标位置处插入指定文件的内容。 |
|[LineDown](selection_linedown) | 把光标下移指定的行数。 |
|[LineOpen](selection_lineopen) | 在两行之间插入一个空行。 |
|[LineUp](selection_lineup) | 把光标上移指定的行数。 |
|[NewLine](selection_newline) | 在光标处插入指定的新行数。 |
|[NextBookmark](selection_nextbookmark) | 移动到文档中的下一个书签处。 |
|[OpenLink](selection_openlink) | 打开光标处的超链接。 |
|[PageDown](selection_pagedown) | 在文档中，把光标下移指定的页数。 |
|[PageUp](selection_pageup) | 在文档中，把光标上移指定的页数。 |
|[Paste](selection_paste) | 在光标处插入剪贴板内容。 |
|[PreviousBookmark](selection_previousbookmark) | 移动到文档中的上一个书签处。 |
|[Replace](selection_replace) | 在文档中替换一个字符串。 |
|[SelectAll](selection_selectall) | 选择整个文档。 |
|[SelectColumn](select_column) | 在 CSV 模式中选择指定的列。 |
|[SelectLine](selection_selectline) | 在光标处选择一行。 |
|[SelectWord](selection_selectword) | 选择光标处的整个单词。 |
|[SetActivePoint](selection_setactivepoint) | 移动光标位置并选择性地扩展选定内容。 |
|[SetAnchorPoint](selection_setanchorpoint) | 设置选定内容的原点。 |
|[SetBookmark](selection_setbookmark) | 在光标位置处设一个书签。 |
|[Sort](sort) | 排序或删除选区内的重复的拆分字符串。 |
|[StartOfDocument](selection_startofdocument) | 把光标移动到文档的开始位置。 |
|[StartOfLine](selection_startofline) | 把光标移动到行首。 |
|[Tabify](selection_tabify) | 把选定内容中的空格转换为 tab。 |
|[TagJump](selection_tagjump) | 跳转到光标所在的标签。 |
|[UnIndent](selection_unindent) | 按指定的缩进等级数从被选取的文本中删除缩进。 |
|[Untabify](selection_untabify) | 把选定内容中的 tab 转换为空格。 |
|[WordLeft](selection_wordleft) | 把光标向左移指定的单词数。 |
|[WordRight](selection_wordright) | 把光标向右移指定的单词数。 |

## 版本

支持 EmEditor 4.00 或之后的版本。


```{toctree}
:maxdepth: 1
average
batch_find
batch_replace
extract_frequent
select_column
selection_changecase
selection_changewidth
selection_charleft
selection_charright
selection_clearbookmark
selection_collapse
selection_copy
selection_copylink
selection_count
selection_cut
selection_delete
selection_deleteleft
selection_destructiveinsert
selection_duplicateline
selection_endofdocument
selection_endofline
selection_find
selection_findrepeat
selection_format
selection_getactivepointx
selection_getactivepointy
selection_getanchorpointx
selection_getanchorpointy
selection_getbottompointx
selection_getbottompointy
selection_gettoppointx
selection_gettoppointy
selection_gotobrace
selection_indent
selection_insertdate
selection_insertfromfile
selection_isactiveendgreater
selection_isempty
selection_linedown
selection_lineopen
selection_lineup
selection_mode
selection_newline
selection_nextbookmark
selection_openlink
selection_overwritemode
selection_pagedown
selection_pageup
selection_paste
selection_previousbookmark
selection_replace
selection_selectall
selection_selectline
selection_selectword
selection_setactivepoint
selection_setanchorpoint
selection_setbookmark
selection_startofdocument
selection_startofline
selection_tabify
selection_tagjump
selection_text
selection_unindent
selection_untabify
selection_wordleft
selection_wordright
sort
sum
```
