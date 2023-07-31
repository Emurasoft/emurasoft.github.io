# Window オブジェクト

## プロパティ

|     |     |
| --- | --- |
| [Caption](caption) | ウィンドウのキャプション テキストを返します。 |
| [Children](children) | 子ウィンドウを表現する Windows コレクションを返します。 |
| [ClassName](class_name) | ウィンドウのクラス名を返します。 |
| [clipboardData](clipboarddata) | clipboardData オブジェクトを取得します。 |
| [CombineHistory](combine_history) | 元に戻す/やり直しの履歴を組み合わせるかどうかを指定します。 |
| [DiscardUndo](discard_undo) | EmEditor が置換、挿入、削除の速度を改善するために元に戻す情報を破棄するかどうかを示すフラグを取得します。 |
| [document](window_document) | 現在開いている Document オブジェクトを返します。 |
| [DroppedFiles](droppedfiles) | DroppedFiles コレクションを返します。 |
| [editor](window_editor) | Editor オブジェクトを返します。 |
| [Enabled](enabled) | ウィンドウでマウスとキーボードの入力が有効かどうかを返します。 |
| [ExStyle](exstyle) | 指定したウィンドウの拡張スタイルを返します。 |
| [Height](height) | ウィンドウの高さを取得するか、または設定します。 |
| [hWnd](hwnd) | ウィンドウのハンドル値を取得するか、または設定します。 |
| [Interface](interface) | Interface オブジェクトを返します。 |
| [LeftX](leftx) | 指定したウィンドウの水平方向の位置をピクセル単位で返すか、または設定します。 |
| [OutputBar](output_bar) | OutputBar オブジェクトを返します。 |
| [Parent](parent) | 親の Window オブジェクトを返します。 |
| [ProcessID](process_id) | プロセス ID を返します。 |
| [Redraw](window_redraw) | ウィンドウの再描画を行うかどうかを指定します。 |
| [ScriptFullName](scriptfullname) | 現在実行しているマクロの完全パスと名前を取得します。 |
| [ScriptName](scriptname) | 現在実行しているマクロのファイル名をパスを付けないで取得します。 |
| [scrollX](window_scrollx) | スクロール バーの水平方向の位置を 1 から始まる整数で返します。 |
| [scrollY](window_scrolly) | スクロール バーの垂直方向の位置を 1 から始まる整数で返します。 |
| [shell](shell) | Shell オブジェクトを返します。 |
| [status](window_status) | ステータス バーに表示する文字列を取得、または設定します。 |
| [Style](style) | 指定したウィンドウのスタイルを返します。 |
| [ThreadID](thread_id) | ウィンドウを作成したスレッド ID を返します。 |
| [Top](top) | 指定したウィンドウの垂直方向をピクセル単位で返すか、または設定します。 |
| [Valid](valid) | ウィンドウのハンドルが有効かどうかを返します。 |
| [Visible](visible) | ウィンドウが表示されている状態かどうかを返します。 |
| [Width](width) | ウィンドウの幅を取得するか、または設定します。 |

## メソッド

|     |     |
| --- | --- |
| [alert](window_alert) | \[OK\] ボタンが付いたダイアログ ボックス内にメッセージを表示します。 |
| [close](window_close) | ウィンドウを閉じます。 |
| [confirm](window_confirm) | \[OK\] ボタンと \[キャンセル\] ボタンが付いたダイアログ ボックス内にメッセージを表示します。 |
| [CreatePopupMenu](createpopupmenu) | ポップアップ メニューを作成します。 |
| [FindWindow](find_window) | クラス名と/またはウィンドウのタイトルで子 window オブジェクトを検索します。 |
| [FindWindowByID](find_window_by_id) | ウィンドウの識別子で子ウィンドウ オブジェクトを見つけます。 |
| [print](window_print) | 印刷ダイアログを表示します。 |
| [prompt](window_prompt) | 文字列を入力するためのダイアログ ボックスを表示します。 |
| [Quit](quit) | マクロの実行を停止します。 |
| [scrollBy](window_scrollby) | スクロール バーを指定する差分だけ移動します。 |
| [scrollTo](window_scrollto) | スクロール バーを指定する位置に移動します。 |
| [SetFocus](set_focus) | ウィンドウにキーボード フォーカスを設定します。 |
| [SetForeground](set_foreground) | フォアグラウンドにウィンドウを持ってきます。 |
| [SetPosition](set_position) | ウィンドウのサイズと位置を設定します。 |
| [ShowTip](show_tip) | ツールチップを表示します。 |
| [Sleep](window_sleep) | ミリ秒で指定する時間だけマクロの実行を停止します。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。


```{toctree}
:hidden:
:maxdepth: 1
caption
children
class_name
clipboarddata
combine_history
createpopupmenu
discard_undo
droppedfiles
enabled
exstyle
find_window
find_window_by_id
height
hwnd
interface
leftx
output_bar
parent
process_id
quit
scriptfullname
scriptname
set_focus
set_foreground
set_position
shell
show_tip
style
thread_id
top
valid
visible
width
window_alert
window_close
window_confirm
window_document
window_editor
window_print
window_prompt
window_redraw
window_scrollby
window_scrollto
window_scrollx
window_scrolly
window_sleep
window_status
```
