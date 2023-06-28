# Selection オブジェクト

## プロパティ

|     |     |
| --- | --- |
| [Average](average) | 選択範囲に含まれる数の平均を取得します。 |
| [Count](selection_count) | 現在の文書中にある選択の個数を返します。 |
| [IsActiveEndGreater](selection_isactiveendgreater) | カーソル位置が選択範囲の最後と一致しているかどうかを示します。 |
| [IsEmpty](selection_isempty) | 選択範囲が空かどうかを示します。 |
| [Mode](selection_mode) | 選択の種類 (箱型選択、行選択など) を取得、または設定します。 |
| [OverwriteMode](selection_overwritemode) | 上書き状態、または挿入状態かどうかを取得、または設定します。 |
| [Sum](sum) | 選択範囲に含まれる数の合計を取得します。 |
| [Text](selection_text) | 選択されたテキストを取得、またはテキストを挿入します。 |

## メソッド

|     |     |
| --- | --- |
| [BatchFind](batch_find) | 複数の文字列を検索します。 |
| [BatchReplace](batch_replace) | 複数の文字列を置き換えます。 |
| [ChangeCase](selection_changecase) | 選択されたテキストの大文字と小文字を変換します。 |
| [ChangeWidth](selection_changewidth) | 半角文字と全角文字を変換します。 |
| [CharLeft](selection_charleft) | カーソル位置を左に指定した文字数だけ移動します。 |
| [CharRight](selection_charright) | カーソル位置を右に指定した文字数だけ移動します。 |
| [ClearBookmark](selection_clearbookmark) | 現在行のブックマークを解除します。 |
| [Collapse](selection_collapse) | 選択を解除します。 |
| [Copy](selection_copy) | 選択範囲のテキストをクリップボードにコピーします。 |
| [CopyLink](selection_copylink) | カーソル位置のハイパーリンクをクリップボードにコピーします。 |
| [Cut](selection_cut) | 選択範囲を削除してクリップボードにコピーします。 |
| [Delete](selection_delete) | 選択範囲を削除します。選択が空の場合は、右側の指定した文字数だけ削除します。 |
| [DeleteLeft](selection_deleteleft) | 選択範囲を削除します。選択が空の場合は、左側の指定した文字数だけ削除します。 |
| [DestructiveInsert](selection_destructiveinsert) | 既に存在するテキストを上書きしてテキストを挿入します。 |
| [DuplicateLine](selection_duplicateline) | 現在行を 2 重化します。 |
| [EndOfDocument](selection_endofdocument) | カーソル位置を文書の最後に移動します。 |
| [EndOfLine](selection_endofline) | 現在行の最後に移動します。 |
| [ExtractFrequent](extract_frequent) | 頻出文字列を抽出して新規文書を作成します。 |
| [Find](selection_find) | 指定した文字列を検索します。 |
| [FindRepeat](selection_findrepeat) | 前回検索した文字列を再度検索します。 |
| [Format](selection_format) | 選択範囲の折り返し位置に改行コードの挿入したり、改行コードを削除したりします。 |
| [GetActivePointX](selection_getactivepointx) | カーソル位置の現在桁を 1 で始まる整数で返します。 |
| [GetActivePointY](selection_getactivepointy) | カーソル位置の現在行を 1 で始まる整数で返します。 |
| [GetAnchorPointX](selection_getanchorpointx) | 選択範囲の開始位置の現在桁を 1 で始まる整数で返します。 |
| [GetAnchorPointY](selection_getanchorpointy) | 選択範囲の開始位置の現在行を 1 で始まる整数で返します。 |
| [GetBottomPointX](selection_getbottompointx) | 選択範囲の最後の現在桁を 1 で始まる整数で返します。 |
| [GetBottomPointY](selection_getbottompointy) | 選択範囲の最後の現在行を 1 で始まる整数で返します。 |
| [GetTopPointX](selection_gettoppointx) | 選択範囲の最初の現在桁を 1 で始まる整数で返します。 |
| [GetTopPointY](selection_gettoppointy) | 選択範囲の最初の現在行を 1 で始まる整数で返します。 |
| [GoToBrace](selection_gotobrace) | 対応するかっこへ移動します。 |
| [Indent](selection_indent) | 選択範囲をインデントします。 |
| [InsertDate](selection_insertdate) | 時刻と日付を挿入します。 |
| [InsertFromFile](selection_insertfromfile) | 指定したファイルの中身をカーソル位置に挿入します。 |
| [LineDown](selection_linedown) | カーソル位置を下に指定した行数だけ移動します。 |
| [LineOpen](selection_lineopen) | 行と行の間に改行コードを挿入して空けます。 |
| [LineUp](selection_lineup) | カーソル位置を上に指定した行数だけ移動します。 |
| [NewLine](selection_newline) | カーソル位置に改行コードを挿入します。 |
| [NextBookmark](selection_nextbookmark) | 開いている文書の次のブックマークに移動します。 |
| [OpenLink](selection_openlink) | カーソル位置のハイパーリンクを開きます。 |
| [PageDown](selection_pagedown) | 1 ページ下へ移動します。 |
| [PageUp](selection_pageup) | 1 ページ上へ移動します。 |
| [Paste](selection_paste) | クリップボードの中身をカーソル位置に貼り付けます。 |
| [PreviousBookmark](selection_previousbookmark) | 開いている文書の前のブックマークへ移動します。 |
| [Replace](selection_replace) | 指定した文字列を指定した文字列に置き換えます。 |
| [SelectAll](selection_selectall) | 開いている文書の全体を選択します。 |
| [SelectColumn](select_column) | CSV モードで指定された列を選択します。 |
| [SelectLine](selection_selectline) | カーソル位置の行を選択します。 |
| [SelectWord](selection_selectword) | カーソル位置にある単語を選択します。 |
| [SetActivePoint](selection_setactivepoint) | カーソル位置を設定します。 |
| [SetAnchorPoint](selection_setanchorpoint) | 選択範囲の開始位置を設定します。 |
| [SetBookmark](selection_setbookmark) | カーソル位置にブックマークを設定します。 |
| [Sort](sort) | 選択範囲の分割文字列を並べ替え、または重複した分割文字列を削除します。 |
| [StartOfDocument](selection_startofdocument) | カーソル位置を文書の最初に移動します。 |
| [StartOfLine](selection_startofline) | カーソル位置を行の最初に移動します。 |
| [Tabify](selection_tabify) | 選択範囲の空白を Tab に変換します。 |
| [TagJump](selection_tagjump) | 現在行のタグにジャンプします。 |
| [UnIndent](selection_unindent) | 選択範囲の逆インデントを行います。 |
| [Untabify](selection_untabify) | 選択範囲の Tab を空白に変換します。 |
| [WordLeft](selection_wordleft) | カーソル位置を単語の左に移動します。 |
| [WordRight](selection_wordright) | カーソル位置を単語の右に移動します。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。

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
