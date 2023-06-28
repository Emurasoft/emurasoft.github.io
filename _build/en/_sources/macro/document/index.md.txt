# Document 對象

## 屬性

|     |     |
| --- | --- |
| **[ActiveString](active_string)** | 在游標停留處檢索主動字串。 |
| **[BookmarkCount](bookmark_count)** | 檢索文檔中的書籤數。 |
| **[CellMode](cell_mode)** | 設定或檢索一個標志來顯示選擇模式是否是儲存格選擇模式。 |
| **[Config](config)** | 檢索 Config 對象。 |
| **[Csv](csv)** | 檢索 Csv 對象。 |
| **[ConfigName](document_configname)** | 檢索或設定目前的組態名稱。 |
| **[Encoding](document_encoding)** | 檢索或設定打開的檔案的目前的編碼。 |
| **[filters](filters)** | 檢索或設定 [**Filters** 集合](../filters/index)。 |
| **[FontCategory](document_fontcategory)** | 檢索或設定目前的字型類別。 |
| **[FullName](document_fullname)** | 檢索文檔的完整路徑以及檔案名稱。 |
| **[HeadingLines](heading_lines)** | 檢索或設定標題的行數 (不能捲動的區域)。 |
| **[HideQuotes](hide_quotes)** | 檢索或設定一個標志，該標志指示在 CSV 儲存格選擇模式下是否啟用了「隱藏引號」顯示畫面。 |
| **[HighlightFind](document_hightlightfind)** | 決定是否要亮顯搜尋字串。 |
| **[HighlightTag](document_hightlighttag)** | 決定是否要亮顯標籤。 |
| **[MemorySize](memory_size)** | 檢索或設定使用的記憶體大小。 |
| **[Name](document_name)** | 檢索不帶路徑的文檔的檔案名，或重新命名文檔的檔案名。如果文檔沒有標題，則重新命名文檔標題而不儲存檔案。 |
| **[NarrowingTop](narrowing_top)** | 檢索或設定僅編輯區域的頂部 ( y 軸)。 |
| **[NarrowingBottom](narrowing_bottom)** | 檢索或設定僅編輯區域的底部 ( y 軸)。 |
| **[NewlineCode](newline_code)** | 檢索文檔的目前的新行字元碼。 |
| **[Path](document_path)** | 僅檢索目前的文檔的路徑。 |
| **[ReadOnly](document_readonly)** | 設定文檔的唯讀狀態。 |
| **[Saved](document_saved)** | 檢索或設定表示自從上次被儲存或打開後文檔是否已被修改的標志。 |
| **[selection](document_selection)** | 檢索 Selection 對象. |
| **[Title](title)** | 檢索或設定文檔標題。 |
| **[UnicodeSignature](document_unicodesignature)** | 檢索或設定標志，表示 EmEditor 是否應添加 Unicode 簽名 (BOM) 當下次儲存該文檔時。 |
| **[Untitled](untitled)** | 檢索標示文檔是否未命名的標志。 |

## 方法

|     |     |
| --- | --- |
| **[Activate](document_activate)** | 啟動文檔。 |
| **[Close](document_close)** | 關閉文檔。 |
| **[CombineColumns](combinecolumns)** | 在 CSV 模式下合併指定欄。 |
| **[CombineLines](combine_lines)** | 合併 CSV 文檔中垂直相鄰的重複儲存格。 |
| **[ConvertCsv](convert_csv)** | 轉換 CSV 格式。 |
| **[DeleteColumn](delete_column)** | 刪除 CSV 模式中指定的欄。 |
| **[CopyFullName](document_copyfullname)** | 複製文檔的完整路徑以及檔案名稱到剪貼簿上。 |
| **[CopyPath](document_copypath)** | 僅複製文檔的路徑到剪貼簿上。 |
| **[DeleteDuplicates](delete_duplicates)** | 刪除重複行，或把重複行設為書籤。 |
| **[ExtractColumns](extract_columns)** | 抽出 CSV 文檔中的指定欄。 |
| **[Filter](filter)** | 用指定的字串以及設定來篩選文檔。 |
| **[GetCell](getcell)** | 在 CSV 模式中指定的儲存格中檢索文字。 |
| **[GetColumn](getcolumn)** | 在 CSV 模式中檢索文字欄。 |
| **[GetColumns](getcolumns)** | 在 CSV 模式中檢索欄數。 |
| **[GetLine](getline)** | 檢索指定行上的文字。 |
| **[GetLines](getlines)** | 檢索文檔中的行數。 |
| **[InsertColumn](insertcolumn)** | 在 CSV 模式下插入文字列。 |
| **[LogicalToSerial](logicaltoserial)** | 將指定位置的邏輯座標轉換為基於單個的串行位置。 |
| **[LogicalToView](logicaltoview)** | 將指定位置的邏輯座標轉換為顯示座標，並檢索 [**Point** 對象](../point/index) 中的位置。 |
| **[MoveColumn](movecolumn)** | 在 CSV 模式下移動或複製指定欄。 |
| **[Numbering](numbering)** | 在游標位置或垂直選擇處，插入編號。 |
| [**PivotTable**](pivot_table) | 在 CSV 文檔中建立樞紐分析表。 |
| [**RearrangeColumns**](rearrange_columns) | 重排 CSV 欄。 |
| **[Redo](document_redo)** | 用 [**Undo** 命令](../../cmd/edit/edit_undo) 重做上次復原的動作。 |
| **[Save](document_save)** | 儲存文檔。 |
| **[SerialToLogical](serialtological)** | 將串行位置轉換為邏輯座標，並檢索在 [**Point** 對象](../point/index) 中的位置。 |
| **[SetCell](setcell)** | 在 CSV 模式下指定的儲存格中設定文字。 |
| **[SetColumn](setcolumn)** | 在 CSV 模式下設定文字列。 |
| **[Sort](sort)** | 排序文檔。 |
| **[SplitColumn](split_column)** | 用指定的分隔符號分割列，並在 CSV 模式下將其放入右邊的欄或下方的行中。 |
| **[Undo](document_undo)** | 復原上一次的動作。 |
| [**Unpivot**](unpivot) | 通過壓平合併 CSV 數據將欄轉換為列。 |
| **[ValidateCsv](validatecsv)** | 驗證 CSV 文檔和匯出錯誤，並可選擇調整分隔符位置。 |
| **[ViewToLogical](viewtological)** | 將指定位置的顯示座標轉換為邏輯座標，並檢索 [**Point** 對象](../point/index) 中的位置。 |
| **[write](document_write)** | 在目前的游標位置處插入或覆寫一個字串。 |
| **[writeln](document_writeln)** | 在目前的游標位置處插入或覆寫一個字串並換行。 |

## 版本

支持 EmEditor 4.00 或之後的版本。

```{toctree}
:maxdepth: 1
active_string
autofill
bookmark_count
cell_mode
combine_lines
combinecolumns
config
convert_csv
csv
delete_column
delete_duplicates
document_activate
document_close
document_configname
document_copyfullname
document_copypath
document_encoding
document_fontcategory
document_fullname
document_hightlightfind
document_hightlighttag
document_name
document_path
document_readonly
document_redo
document_save
document_saved
document_selection
document_undo
document_unicodesignature
document_write
document_writeln
extract_columns
filter
filters
getcell
getcolumn
getcolumns
getline
getlines
heading_lines
hide_quotes
insertcolumn
logicaltoserial
logicaltoview
memory_size
movecolumn
narrowing_bottom
narrowing_top
newline_code
numbering
pivot_table
rearrange_columns
serialtological
setcell
setcolumn
sort
split_column
title
unpivot
untitled
validatecsv
viewtological
```
