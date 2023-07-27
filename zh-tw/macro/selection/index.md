# Selection 對象

## 屬性

|     |     |
| --- | --- |
|[Average](average) | 檢索所選內容中包含的數字的平均值。 |
|[Count](selection_count) | 檢索在目前的文檔中所選取的數目。 |
|[IsActiveEndGreater](selection_isactiveendgreater) | 表示活動點是否與底部點相同。 |
|[IsEmpty](selection_isempty) | 表示活動點是否與錨點相同。 |
|[Mode](selection_mode) | 設置或檢索表示選取模式的標志。 |
|[OverwriteMode](selection_overwritemode) | 設置或檢索表示覆寫或插入模式的標志。 |
|[Sum](sum) | 檢索所選內容中包含的數字的總和。 |
|[Text](selection_text) | 檢索被選取的文字，或在游標位置處插入一個字串。 |

## 方法

|     |     |
| --- | --- |
|[BatchFind](batch_find) | 搜索多個字串。 |
|[BatchReplace](batch_replace) | 取代多個字串。 |
|[ChangeCase](selection_changecase) | 變更所選取的文字的大小寫。 |
|[ChangeWidth](selection_changewidth) | 變更所選取的文字的寬度。 |
|[CharLeft](selection_charleft) | 把游標向左移動指定的字元數。 |
|[CharRight](selection_charright) | 把游標向右移動指定的字元數。 |
|[ClearBookmark](selection_clearbookmark) | 清除目前的行上的書籤。 |
|[Collapse](selection_collapse) | 折疊所選的部分到活動點。 |
|[Copy](selection_copy) | 複製選定內容到剪貼簿上。 |
|[CopyLink](selection_copylink) | 複製游標處的超連結到剪貼簿上。 |
|[Cut](selection_cut) | 把選取的文字移動到剪貼簿上。 |
|[Delete](selection_delete) | 刪除所選內容。 |
|[DeleteLeft](selection_deleteleft) | 刪除所選內容或游標左邊的指定字元數。 |
|[DestructiveInsert](selection_destructiveinsert) | 插入文字，覆蓋已存在的文字。 |
|[DuplicateLine](selection_duplicateline) | 複製目前的行。 |
|[EndOfDocument](selection_endofdocument) | 把游標移到文檔末尾。 |
|[EndOfLine](selection_endofline) | 把游標移到目前的行的尾端。 |
| [ExtractFrequent](extract_frequent) | 將常用字串抽出到新文檔中。 |
|[Find](selection_find) | 搜尋指定的字串。 |
|[FindRepeat](selection_findrepeat) | 對同一個字串重複上一次搜尋。 |
|[Format](selection_format) | 插入或刪除選定內容中的新行。 |
|[GetActivePointX](selection_getactivepointx) | 返回游標位置處的列號。 |
|[GetActivePointY](selection_getactivepointy) | 返回游標位置處的行號。 |
|[GetAnchorPointX](selection_getanchorpointx) | 返回選定內容原點的列號。 |
|[GetAnchorPointY](selection_getanchorpointy) | 返回選定內容原點的行號。 |
|[GetBottomPointX](selection_getbottompointx) | 返回選定內容底部的列號。 |
|[GetBottomPointY](selection_getbottompointy) | 返回選定內容底部的行號。 |
|[GetTopPointX](selection_gettoppointx) | 返回選定內容頂部的列號。 |
|[GetTopPointY](selection_gettoppointy) | 返回選定內容頂部的行號。 |
|[GoToBrace](selection_gotobrace) | 把游標移動到相對應的括號處。 |
|[Indent](selection_indent) | 按指定的縮排等級數來縮排被選取的行。 |
|[InsertDate](selection_insertdate) | 插入目前的時間和日期。 |
|[InsertFromFile](selection_insertfromfile) | 在游標位置處插入指定檔案的內容。 |
|[LineDown](selection_linedown) | 把游標下移指定的行數。 |
|[LineOpen](selection_lineopen) | 在兩行之間插入一個空行。 |
|[LineUp](selection_lineup) | 把游標上移指定的行數。 |
|[NewLine](selection_newline) | 在游標處插入指定的新行數。 |
|[NextBookmark](selection_nextbookmark) | 移動到文檔中的下一個書籤處。 |
|[OpenLink](selection_openlink) | 打開游標處的超連結。 |
|[PageDown](selection_pagedown) | 在文檔中，把游標下移指定的頁數。 |
|[PageUp](selection_pageup) | 在文檔中，把游標上移指定的頁數。 |
|[Paste](selection_paste) | 在游標處插入剪貼簿內容。 |
|[PreviousBookmark](selection_previousbookmark) | 移動到文檔中的上一個書籤處。 |
|[Replace](selection_replace) | 在文檔中取代一個字串。 |
|[SelectAll](selection_selectall) | 選擇整個文檔。 |
|[SelectColumn](select_column) | 在 CSV 模式中選擇指定的欄。 |
|[SelectLine](selection_selectline) | 在游標處選擇一行。 |
|[SelectWord](selection_selectword) | 選擇游標處的整個單字。 |
|[SetActivePoint](selection_setactivepoint) | 移動游標位置并選擇性地延伸選定內容。 |
|[SetAnchorPoint](selection_setanchorpoint) | 設置選定內容的原點。 |
|[SetBookmark](selection_setbookmark) | 在游標位置處設一個書籤。 |
|[Sort](sort) | 排序或刪除選區內的重複的分割字串。 |
|[StartOfDocument](selection_startofdocument) | 把游標移動到文檔的開始位置。 |
|[StartOfLine](selection_startofline) | 把游標移動到行首。 |
|[Tabify](selection_tabify) | 把選定內容中的空白轉換為 tab。 |
|[TagJump](selection_tagjump) | 跳轉到游標所在的標籤。 |
|[UnIndent](selection_unindent) | 按指定的縮排等級數從被選取的文字中刪除縮排。 |
|[Untabify](selection_untabify) | 把選定內容中的 tab 轉換為空白。 |
|[WordLeft](selection_wordleft) | 把游標向左移指定的單字數。 |
|[WordRight](selection_wordright) | 把游標向右移指定的單字數。 |

## 版本

支持 EmEditor 4.00 或之後的版本。


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
