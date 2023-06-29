# Document Object

## Properties

|     |     |
| --- | --- |
| **[ActiveString](active_string)** | Retrieves the active string. |
| **[BookmarkCount](bookmark_count)** | Retrieves the number of bookmarks in the document. |
| **[CellMode](cell_mode)** | Sets or retrieves a flag indicating whether the selection mode is cell selection mode. |
| **[Config](config)** | Retrieves the Config Object. |
| **[ConfigName](document_configname)** | Retrieves or sets the current configuration name. |
| **[Csv](csv)** | Retrieves the Csv Object. |
| **[Encoding](document_encoding)** | Retrieves or sets the current encoding of the opened file. |
| **[filters](filters)** | Retrieves or sets the [**Filters** Collection](../filters/index). |
| **[FontCategory](document_fontcategory)** | Retrieves or sets the current font category. |
| **[FullName](document_fullname)** | Retrieves the complete path and file name of the document. |
| **[HeadingLines](heading_lines)** | Retrieves or sets the number of lines for headings (non-scrollable area). |
| **[HideQuotes](hide_quotes)** | Sets or retrieves a flag indicating whether the Hide Quotes Temporarily mode is enabled in the CSV cell selection mode. |
| **[HighlightFind](document_hightlightfind)** | Determines whether to highlight the searched strings. |
| **[HighlightTag](document_hightlighttag)** | Determines whether to highlight tags. |
| **[MemorySize](memory_size)** | Retrieves or sets the memory size used. |
| **[Name](document_name)** | Retrieves the file name of the document without its path, or renames the file name of the document. If the document is untitled, renames the document title without saving the file. |
| **[NarrowingTop](narrowing_top)** | Retrieves or sets the top position (y-axis) of the narrowing (editable area). |
| **[NarrowingBottom](narrowing_bottom)** | Retrieves or sets the bottom position (y-axis) of the narrowing (editable area). |
| **[NewlineCode](newline_code)** | Retrieves the current newline character code of the document. |
| **[Path](document_path)** | Retrieves only the path of the current document. |
| **[ReadOnly](document_readonly)** | Sets the Read-Only status of the document. |
| **[Saved](document_saved)** | Retrieves or sets the flag indicating whether the document has been <br> modified <br> since last being saved or opened. |
| **[selection](document_selection)** | Retrieves the Selection Object. |
| **[Title](title)** | Retrieves or sets the title of the document. |
| **[UnicodeSignature](document_unicodesignature)** | Retrieves or sets the flag indicating whether EmEditor should add the Unicode <br> signature (BOM) next time it saves the document. |
| **[Untitled](untitled)** | Retrieves a flag indicating whether the document is untitled. |

## Methods

|     |     |
| --- | --- |
| **[Activate](document_activate)** | Activates the document. |
| **[AutoFill](autofill)** | Performs the AutoFill or Flash Fill action on the CSV document. |
| **[Close](document_close)** | Closes the document. |
| **[CombineColumns](combinecolumns)** | Combines specified columns in a CSV mode. |
| **[CombineLines](combine_lines)** | Combines vertical adjacent duplicate cells of the CSV document. |
| **[ConvertCsv](convert_csv)** | Converts the CSV format. |
| **[DeleteColumn](delete_column)** | Deletes specified columns in a CSV mode. |
| **[CopyFullName](document_copyfullname)** | Copies the complete path and file name of the document to the <br> Clipboard. |
| **[CopyPath](document_copypath)** | Copies only the path of the document to the Clipboard. |
| **[DeleteDuplicates](delete_duplicates)** | Deletes duplicate lines, or sets bookmarks on duplicate lines. |
| **[ExtractColumns](extract_columns)** | Extracts the specified columns of the CSV document. |
| **[Filter](filter)** | Filters the document with the specified string and settings. |
| **[GetCell](getcell)** | Retrieves the text on the specified cell in a CSV mode. |
| **[GetColumn](getcolumn)** | Retrieves a column of text in CSV mode. |
| **[GetColumns](getcolumns)** | Retrieves the number of columns in a CSV mode. |
| **[GetLine](getline)** | Retrieves the text on the specified line. |
| **[GetLines](getlines)** | Retrieves the number of the lines in the document. |
| **[InsertColumn](insertcolumn)** | Inserts a column of text in CSV mode. |
| **[LogicalToSerial](logicaltoserial)** | Converts the logical coordinates of a specified position to the one-based serial position. |
| **[LogicalToView](logicaltoview)** | Converts the logical coordinates of a specified position to the display coordinates, and retrieves the position in the [**Point** object](../point/index). |
| **[MoveColumn](movecolumn)** | Moves or copies specified columns in a CSV mode. |
| **[Numbering](numbering)** | Inserts numbering at the cursor position or vertical selection. |
| [**PivotTable**](pivot_table) | Creates a pivot table in the CSV document. |
| [**RearrangeColumns**](rearrange_columns) | Rearranges CSV columns. |
| **[Redo](document_redo)** | Redo the last action undone with the<br> [**Undo** command](../../cmd/edit/edit_undo). |
| **[Save](document_save)** | Saves the document. |
| **[SerialToLogical](serialtological)** | Converts a serial position to the logical coordinates, and retrieves the position in the [**Point** object](../point/index). |
| **[SetCell](setcell)** | Sets the text on the specified cell in a CSV mode. |
| **[SetColumn](setcolumn)** | Sets a column of text in a CSV mode. |
| **[Sort](sort)** | Sorts the document. |
| **[SplitColumn](split_column)** | Splits columns by a specified separator and put them into right columns or lines beneath in a CSV mode. |
| **[Undo](document_undo)** | Undo the last action. |
| [**Unpivot**](unpivot) | Converts columns into rows by flattening the CSV data. |
| **[ValidateCsv](validatecsv)** | Validates the CSV document and output errors, and optionally adjusts separator positions. |
| **[ViewToLogical](viewtological)** | Convert the display coordinates of a specified position to the logical coordinates, and retrieves the position in the [**Point** object](../point/index). |
| **[write](document_write)** | Inserts or overwrites a string at the current cursor position. |
| **[writeln](document_writeln)** | Inserts or overwrites a string and a newline character at the current cursor <br> position. |

## Version

Supported on EmEditor Professional Version 4.00 or later.

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
