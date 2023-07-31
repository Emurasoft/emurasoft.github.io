# Document 对象

## 属性

|     |     |
| --- | --- |
| **[ActiveString](active_string)** | 在鼠标悬停处检索活动字符串。 |
| **[BookmarkCount](bookmark_count)** | 检索文档中的书签数。 |
| **[CellMode](cell_mode)** | 设置或检索一个标志来显示选择模式是否是单元格选择模式。 |
| **[Config](config)** | 检索 Config 对象。 |
| **[ConfigName](document_configname)** | 检索或设置当前配置名称。 |
| **[Csv](csv)** | 检索 Csv 对象。 |
| **[Encoding](document_encoding)** | 检索或设置打开的文件的当前编码。 |
| **[filters](filters)** | 检索或设置 [**Filters** 集合](../filters/index)。 |
| **[FontCategory](document_fontcategory)** | 检索或设置当前字体类别。 |
| **[FullName](document_fullname)** | 检索文档的完整路径以及文件名称。 |
| **[HeadingLines](heading_lines)** | 检索或设置标题的行数 (不能滚动的区域)。 |
| **[HideQuotes](hide_quotes)** | 检索或设置一个标志，该标志指示在 CSV 单元格选择模式下是否启用了“隐藏引号”视图。 |
| **[HighlightFind](document_hightlightfind)** | 决定是否要高亮搜索字符串。 |
| **[HighlightTag](document_hightlighttag)** | 决定是否要高亮标签。 |
| **[MemorySize](memory_size)** | 检索或设置使用的内存大小。 |
| **[Name](document_name)** | 检索不带路径的文档的文件名，或重命名文档的文件名。如果文档没有标题，则重命名文档标题而不保存文件。 |
| **[NarrowingTop](narrowing_top)** | 检索或设置仅编辑区域的顶部 ( y 轴)。 |
| **[NarrowingBottom](narrowing_bottom)** | 检索或设置仅编辑区域的底部 ( y 轴)。 |
| **[NewlineCode](newline_code)** | 检索文档的当前换行字符码。 |
| **[Path](document_path)** | 仅检索当前文档的路径。 |
| **[ReadOnly](document_readonly)** | 设置文档的只读状态。 |
| **[Saved](document_saved)** | 检索或设置表示自从上次被保存或打开后文档是否已被修改的标志。 |
| **[selection](document_selection)** | 检索 Selection 对象. |
| **[Title](title)** | 检索或设置文档标题。 |
| **[UnicodeSignature](document_unicodesignature)** | 检索或设置标志，表示 EmEditor 是否应添加 Unicode 签名 (BOM) 当下次保存该文档时。 |
| **[Untitled](untitled)** | 检索标示文档是否无标题的标志。 |

## 方法

|     |     |
| --- | --- |
| **[Activate](document_activate)** | 激活文档。 |
| **[AutoFill](autofill)** | 对 CSV 文档执行自动填充或快速填充操作。 |
| **[Close](document_close)** | 关闭文档。 |
| **[CombineColumns](combinecolumns)** | 在 CSV 模式下合并指定列。 |
| **[CombineLines](combine_lines)** | 合并 CSV 文档中垂直相邻的重复单元格。 |
| **[ConvertCsv](convert_csv)** | 转换 CSV 格式。 |
| **[DeleteColumn](delete_column)** | 删除 CSV 模式中指定的列。 |
| **[CopyFullName](document_copyfullname)** | 复制文档的完整路径以及文件名称到剪贴板上。 |
| **[CopyPath](document_copypath)** | 仅复制文档的路径到剪贴板上。 |
| **[DeleteDuplicates](delete_duplicates)** | 删除重复行，或把重复行设为书签。 |
| **[ExtractColumns](extract_columns)** | 提取 CSV 文档中的指定列。 |
| **[Filter](filter)** | 用指定的字符串以及设定来筛选文档。 |
| **[GetCell](getcell)** | 在 CSV 模式中指定的单元格中检索文本。 |
| **[GetColumn](getcolumn)** | 在 CSV 模式中检索文本列。 |
| **[GetColumns](getcolumns)** | 在 CSV 模式中检索列数。 |
| **[GetLine](getline)** | 检索指定行上的文本。 |
| **[GetLines](getlines)** | 检索文档中的行数。 |
| **[InsertColumn](insertcolumn)** | 在 CSV 模式下插入文本列。 |
| **[LogicalToSerial](logicaltoserial)** | 将指定位置的逻辑坐标转换为基于单个的串行位置。 |
| **[LogicalToView](logicaltoview)** | 将指定位置的逻辑坐标转换为显示坐标，并检索 [**Point** 对象](../point/index) 中的位置。 |
| **[MoveColumn](movecolumn)** | 在 CSV 模式下移动或复制指定列。 |
| **[Numbering](numbering)** | 在鼠标位置或垂直选择处，插入编号。 |
| [**PivotTable**](pivot_table) | 在 CSV 文档中创建数据透视表。 |
| [**RearrangeColumns**](rearrange_columns) | 重排 CSV 列。 |
| **[Redo](document_redo)** | 用 [**Undo** 命令](../../cmd/edit/edit_undo) 重做上次撤消的动作。 |
| **[Save](document_save)** | 保存文档。 |
| **[SerialToLogical](serialtological)** | 将串行位置转换为逻辑坐标，并检索在 [**Point** 对象](../point/index) 中的位置。 |
| **[SetCell](setcell)** | 在 CSV 模式下指定的单元格中设置文本。 |
| **[SetColumn](setcolumn)** | 在 CSV 模式下设置文本列。 |
| **[Sort](sort)** | 排序文档。 |
| **[SplitColumn](split_column)** | 用指定的分隔符拆分列，并在 CSV 模式下将其放入右边的列或下方的行中。 |
| **[Undo](document_undo)** | 撤消上一次的动作。 |
| [**Unpivot**](unpivot) | 通过平展 CSV 数据将列转换为行。 |
| **[ValidateCsv](validatecsv)** | 验证 CSV 文档和输出错误，并可选择调整分隔符位置。 |
| **[ViewToLogical](viewtological)** | 将指定位置的显示坐标转换为逻辑坐标，并检索 [**Point** 对象](../point/index) 中的位置。 |
| **[write](document_write)** | 在当前光标位置处插入或改写一个字符串。 |
| **[writeln](document_writeln)** | 在当前光标位置处插入或改写一个字符串并换行。 |

## 版本

支持 EmEditor 4.00 或之后的版本。


```{toctree}
:hidden:
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
