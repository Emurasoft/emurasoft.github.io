# Document オブジェクト

## プロパティ

|     |     |
| --- | --- |
| [ActiveString](active_string) | マウス ポインターがポイントしているアクティブな文字列を取得します。 |
| [BookmarkCount](bookmark_count) | 文書内のブックマークの数を取得します。 |
| [CellMode](cell_mode) | CSV セル選択モードかどうかを示すフラグを取得、または設定します。 |
| [Config](config) | Config オブジェクトを取得します。 |
| [ConfigName](document_configname) | 現在の設定の名前を取得、または設定します。 |
| [Csv](csv) | Csv オブジェクトを取得します。 |
| [Encoding](document_encoding) | 次に保存する時に使用されるエンコードを取得、または設定します。 |
| [filters](filters) | Filters コレクションを取得、または設定します。 |
| [FontCategory](document_fontcategory) | フォント分類を取得、または設定します |
| [FullName](document_fullname) | 文書ファイルの完全パスと名前を取得します。 |
| [HeadingLines](heading_lines) | ヘディング (非スクロール領域) の行数を取得、または設定します。 |
| [HideQuotes](hide_quotes) | CSV セル選択モードで、一時的に引用符を非表示にするかどうかを示すフラグを取得、または設定します。 |
| [HighlightFind](document_hightlightfind) | 検索した文字列を強調表示するかどうかを取得、または設定します。 |
| [HighlightTag](document_hightlighttag) | タグを強調表示するかどうかを取得、または設定します。 |
| [MemorySize](memory_size) | 文書で使用されている1かたまりのメモリ サイズを取得します。 |
| [Name](document_name) | 文書のファイル名をパスを付けないで取得するか、または文書のファイル名をリネームします。文書が無題の場合、ファイルを保存しないで文書のタイトルを変更します。 |
| [NarrowingTop](narrowing_top) | 部分編集の最上部の位置 (Y 座標) を取得、または設定します。 |
| [NarrowingBottom](narrowing_bottom) | 部分編集の最下部の位置 (Y 座標) を取得、または設定します。 |
| [NewlineCode](newline_code) | 文書の改行コードを取得します。 |
| [Path](document_path) | 文書を含むディレクトリのパスをファイル名を付けないで取得します。 |
| [ReadOnly](document_readonly) | 文書が書き換え禁止状態かどうかを取得、または設定します。 |
| [Saved](document_saved) | 文書を前回保存または開いた後に変更されているかどうかを示すフラグを取得、または設定します。 |
| [selection](document_selection) | Selection オブジェクトを取得します。 |
| [Title](title) | 文書のタイトルを取得、または設定します。 |
| [UnicodeSignature](document_unicodesignature) | 次に保存する時に Unicode サイン (BOM) を付けるかどうかを取得、または設定します。 |
| [Untitled](untitled) | 無題かどうかを示すフラグを取得します。 |

## メソッド

|     |     |
| --- | --- |
| [Activate](document_activate) | 文書をアクティブにします。 |
| [AutoFill](autofill) | CSV 文書に対してオートフィル、またはフラッシュ フィルを実行します。 |
| [close](document_close) | 文書を閉じます。 |
| [CombineColumns](combinecolumns) | CSV モードで指定された列を結合します。 |
| [CombineLines](combine_lines) | CSV 文書の上下隣の重複したセルを結合します。 |
| [ConvertCsv](convert_csv) | CSV形式を変換します。 |
| [CopyFullName](document_copyfullname) | 文書ファイルの完全パスをクリップボードにコピーします。 |
| [CopyPath](document_copypath) | 文書を含むディレクトリのパスをファイル名を付けないでクリップボードにコピーします。 |
| [DeleteColumn](delete_column) | CSV モードで指定された列を削除します。 |
| [DeleteDuplicates](delete_duplicates) | 重複行を削除またはブックマークします。 |
| [ExtractColumns](extract_columns) | CSV 文書から指定する列を抽出して新規文書を作成します。 |
| [Filter](filter) | 指定する文字列と設定で文書にフィルターをかけます。 |
| [GetCell](getcell) | CSV モードで指定するセルのテキストを取得します。 |
| [GetColumn](getcolumn) | CSV モードで指定する列の文字列を取得します。 |
| [GetColumns](getcolumns) | CSV モードで列の数を取得します。 |
| [GetLine](getline) | 指定する行のテキストを取得します。 |
| [GetLines](getlines) | 文書全体の行数を取得します。 |
| [InsertColumn](insertcolumn) | CSV モードで指定する列位置に新しい列を挿入します。 |
| [LogicalToSerial](logicaltoserial) | 論理座標をシリアル位置に変換します。 |
| [LogicalToView](logicaltoview) | 論理座標を表示座標に変換します。 |
| [MoveColumn](movecolumn) | CSV モードで指定された列を移動またはコピーします。 |
| [Numbering](numbering) | カーソル位置または垂直選択に番号を挿入します。 |
| [PivotTable](pivot_table) | CSV文書でピボット テーブルを作成します。 |
| [RearrangeColumns](rearrange_columns) | CSV 列を再配置します。 |
| [Redo](document_redo) | \[元に戻す\] コマンドのやり直しを行います。 |
| [Save](document_save) | 文書を保存します。 |
| [SerialToLogical](serialtological) | シリアル位置を論理座標に変換します。 |
| [SetCell](setcell) | CSV モードで指定するセルに文字列を設定します。 |
| [SetColumn](setcolumn) | CSV モードで指定する列に文字列を設定します。 |
| [Sort](sort) | 文書を並べ替えます。 |
| [SplitColumn](split_column) | CSV モードで指定された列を区切り文字で分割して右の列または下の行に置きます。 |
| [Undo](document_undo) | 直前の操作を元に戻します。 |
| [Unpivot](unpivot) | CSVデータを平らにして行に変換します。 |
| [ValidateCsv](validatecsv) | CSV文書の正当性を確認してエラーを出力し、オプションにより区切り位置を調節します。 |
| [ViewToLogical](viewtological) | 表示座標を論理座標に変換します。 |
| [write](document_write) | 現在のカーソル位置に文字列を挿入、または上書きします。 |
| [writeln](document_writeln) | 現在のカーソル位置に文字列と改行コードを挿入、または上書きします。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。


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
