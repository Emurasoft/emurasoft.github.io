# メッセージ

メッセージは、プラグインからEmEditorに指定したタスクを送るときに使用されます。

| メッセージ | 説明 |
| --- | --- |
| [EE\_ADD\_REF](ee_add_ref) | プラグインの参照数を1つ増加させます。 |
| [EE\_AUTOFILL](ee_autofill) | プラグインの参照数を1つ増加させます。 |
| [EE\_CLIP\_HISTORY](ee_clip_history) | クリップボードの履歴を操作します。 |
| [EE\_COMPARE](ee_compare) | 2個の文書を比較します。 |
| [EE\_CONVERT](ee_convert) | 文字変換を行います。 |
| [EE\_CONVERT\_CSV](ee_convert_csv) | 現在の文書のCSV形式を変換します。 |
| [EE\_CONVERT\_EX](ee_convert_ex) | 文字変換を行います。 |
| [EE\_CUSTOM\_BAR\_OPEN](ee_custom_bar_open) | カスタム バーを開きます。 |
| [EE\_CUSTOM\_BAR\_CLOSE](ee_custom_bar_close) | カスタム バーを閉じます。 |
| [EE\_DEV\_TO\_VIEW](ee_dev_to_view) | デバイス座標 (クライアント座標) を表示座標に変換します。 |
| [EE\_DO\_IDLE](ee_do_idle) | ツール バー、タイトル、タブなどの表示更新を行います。 |
| [EE\_EDIT\_COLUMN](ee_edit_column) | 現在の CSV 文書の指定された列を移動、コピー、削除、または結合します。 |
| [EE\_EDIT\_TEMP](ee_edit_temp) | 一時テキストを新規文書として開くか、アクティブにするか、保存するか、または閉じます。 |
| [EE\_EMPTY\_UNDO\_BUFFER](ee_empty_undo_buffer) | 元に戻す、やり直しのバッファを空にします。 |
| [EE\_ENUM\_CONFIG](ee_enum_config) | 利用可能な設定の一覧を取得します。 |
| [EE\_ENUM\_HIGHLIGHT](ee_enum_highlight) | 強調文字列の一覧を取得します。 |
| [EE\_EXEC\_COMMAND](ee_exec_command) | 指定するコマンドIDを実行します |
| [EE\_EXEC\_PLUGIN](ee_exec_plugin) | 指定するプラグインを実行します |
| [EE\_EXTRACT\_FREQUENT](ee_extract_frequent) | 頻出文字列を抽出して新規文書を作成します。 |
| [EE\_FILTER](ee_filter) | 指定する文字列と設定で文書にフィルターをかけます。 |
| [EE\_FINDA](ee_finda) | ANSI 文字列を検索します。 |
| [EE\_FINDW](ee_findw) | Unicode文字列を検索します。 |
| [EE\_FIND\_IN\_FILESA](ee_find_in_filesa) | 指定するパスの複数のファイルから ANSI 文字列を検索します。 |
| [EE\_FIND\_IN\_FILESW](ee_find_in_filesw) | 指定するパスの複数のファイルから Unicode 文字列を検索します。 |
| [EE\_FIND\_REGEX](ee_find_regex) | 正規表現を指定して文字列から検索します。 |
| [EE\_FIND\_REPLACE](ee_find_replace) | 文字列を検索または置換します。 |
| [EE\_FREE](ee_free) | プラグインを開放します。 |
| [EE\_GET\_ACCEL\_ARRAY](ee_get_accel_array) | ショートカット キーの配列を取得します。 |
| [EE\_GET\_ACTIVE\_STRING](ee_get_active_string) | Retrieves the active string. |
| [EE\_GET\_ANCHOR\_POS](ee_get_anchor_pos) | カーソル位置を取得します。 |
| [EE\_GET\_ATTR](ee_get_attr) | 構成を取得して、指定した位置に返します。 |
| [EE\_GET\_CARET\_POS](ee_get_caret_pos) | カーソル位置を取得します。 |
| [EE\_GET\_CELL](ee_get_cell) | 指定するセルのUnicodeテキストを取得します。 |
| [EE\_GET\_CMD\_ID](ee_get_cmd_id) | プラグインのコマンドIDを取得します。 |
| [EE\_GET\_COLOR](ee_get_color) | 指定する部分の文字色、背景色、スタイルを取得します。 |
| [EE\_GET\_COLUMN](ee_get_column) | CSV モードで指定する列の文字列を取得します。 |
| [EE\_GET\_CONFIGA](ee_get_configa) | 選択されている設定の名前をANSI文字列で取得します。 |
| [EE\_GET\_CONFIGW](ee_get_configw) | 選択されている設定の名前をUnicode文字列で取得します。 |
| [EE\_GET\_DROPPED\_FILE](ee_get_dropped_file) | 最近ドロップされたファイルを取得します。 |
| [EE\_GET\_FILTER](ee_get_filter) | 現在の文書にかけられているフィルターの文字列と設定を取得します。 |
| [EE\_GET\_LINEA](ee_get_linea) | 指定する行のANSIテキストを取得します。 |
| [EE\_GET\_LINES](ee_get_lines) | テキスト全体の行数を取得します。 |
| [EE\_GET\_LINEW](ee_get_linew) | 指定する行のUnicodeテキストを取得します。 |
| [EE\_GET\_MARGIN](ee_get_margin) | 折り返し桁数を返します。 |
| [EE\_GET\_MODIFIED](ee_get_modified) | 文書が更新されているかどうかのフラグを取得します。 |
| [EE\_GET\_MULTI\_SEL](ee_get_multi_sel) | 複数選択が利用可能な場合、指定する選択の情報を取得します。 |
| [EE\_GET\_OUTLINE\_LEVEL](ee_get_outline_level) | 指定する論理行のアウトラインのレベルを取得します。 |
| [EE\_GET\_OUTPUT\_STRING](ee_get_output_string) | アウトプット バーにあるテキストを取得します。 |
| [EE\_GET\_PAGE\_SIZE](ee_get_page_size) | 1ページのサイズを取得します。 |
| [EE\_GET\_REDRAW](ee_get_redraw) | ウィンドウの再描画を行うかどうかのフラグを取得します。 |
| [EE\_GET\_REF](ee_get_ref) | 指定するプラグインの参照数を返します。 |
| [EE\_GET\_SCROLL\_POS](ee_get_scroll_pos) | スクロール バーの位置を取得します。 |
| [EE\_GET\_SEL\_END](ee_get_sel_end) | 選択テキストの終了位置を取得します。 |
| [EE\_GET\_SEL\_START](ee_get_sel_start) | 選択テキストの開始位置を取得します。 |
| [EE\_GET\_SEL\_TEXTA](ee_get_sel_texta) | 選択されているANSIテキストを取得します。 |
| [EE\_GET\_SEL\_TEXTW](ee_get_sel_textw) | 選択されているUnicodeテキストを取得します。 |
| [EE\_GET\_SEL\_TYPE](ee_get_sel_type) | 選択状態の種類を取得します。 |
| [EE\_GET\_STATUSA](ee_get_statusa) | ステータス バーに表示されている文字列をANSIで取得します。 |
| [EE\_GET\_STATUSW](ee_get_statusw) | ステータス バーに表示されている文字列をUnicodeで取得します。 |
| [EE\_GET\_UNICODE\_NAME](ee_get_unicode_name) | 指定された文字または文字列のUnicode名を取得します。 |
| [EE\_GET\_VERSION](ee_get_version) | バージョン番号を返します。 |
| [EE\_GET\_WORD](ee_get_word) | カーソル位置の単語を返します。 |
| [EE\_HELP](ee_help) | 指定するヘルプのページを表示します。 |
| [EE\_INFO](ee_info) | 実行中のEmEditorに関する情報を取得または設定を行います。 |
| [EE\_INFO\_EX](ee_info_ex) | 実行中のEmEditorに関する情報を取得または設定を行います。 |
| [EE\_INSERT\_FILEA](ee_insert_filea) | 指定するファイルの中身をカーソル位置に挿入します(ANSI)。 |
| [EE\_INSERT\_FILEW](ee_insert_filew) | 指定するファイルの中身をカーソル位置に挿入します(Unicode)。 |
| [EE\_INSERT\_STRINGA](ee_insert_stringa) | カーソル位置にANSI文字列を挿入します。 |
| [EE\_INSERT\_STRINGW](ee_insert_stringw) | カーソル位置にUnicode文字列を挿入します。 |
| [EE\_IS\_CHAR\_HALF\_OR\_FULL](ee_is_char_half_or_full) | 指定する文字が半角か全角かを調べます。 |
| [EE\_JOIN](ee_join) | SQL においての JOIN 操作と同様な方法を使って、2個の CSV 文書を結合して新規文書を作成します。 |
| [EE\_KEYBOARD\_PROP](ee_keyboard_prop) | 指定したコマンド ID と設定のキーボード プロパティを表示します。 |
| [EE\_LINE\_FROM\_CHAR](ee_line_from_char) | 指定したシリアル位置の行番号を返します。 |
| [EE\_LINE\_INDEX](ee_line_index) | 指定した行番号のシリアル位置を返します。 |
| [EE\_LOAD\_CONFIGA](ee_load_configa) | ANSI文字列で指定する設定を読み直します。 |
| [EE\_LOAD\_CONFIGW](ee_load_configw) | Unicode文字列で指定する設定を読み直します。 |
| [EE\_LOAD\_FILEA](ee_load_filea) | 文書を指定するファイルから読みこんで表示します (ANSI)。 |
| [EE\_LOAD\_FILEW](ee_load_filew) | 文書を指定するファイルから読みこんで表示します (Unicode)。 |
| [EE\_LOGICAL\_TO\_SERIAL](ee_logical_to_serial) | 論理座標をシリアル位置に変換します。 |
| [EE\_LOGICAL\_TO\_VIEW](ee_logical_to_view) | 論理座標を表示座標に変換します。 |
| [EE\_MANAGE\_DUPLICATES](ee_manage_duplicates) | 重複行を削除またはブックマークします。。 |
| [EE\_MATCH\_REGEX](ee_match_regex) | 正規表現で指定する文字列が一致するかどうかを調べます。 |
| [EE\_NUMBERING](ee_numbering) | カーソル位置または垂直選択に番号を挿入します。 |
| [EE\_OUTPUT\_DIR](ee_output_dir) | アウトプット バーにカレント ディレクトリを設定します。 |
| [EE\_OUTPUT\_STRING](ee_output_string) | アウトプット バーに文字列を追加します。 |
| [EE\_PIVOT\_TABLE](ee_pivot_table) | CSV 文書のピボット テーブルを作成します。 |
| [EE\_QUERY\_STATUS](ee_query_status) | 指定するコマンドIDが実行可能か、またはチェックされた状態かを調べます。 |
| [EE\_QUERY\_STRING](ee_query_string) | 指定するコマンドに関連する文字列を取得します。 |
| [EE\_QUERY\_STRING\_EX](ee_query_string_ex) | 指定するコマンドに関連する文字列を取得します。このメッセージは MAX\_PATH 文字を超える長いファイル パスをサポートしています。 |
| [EE\_REARRANGE\_COLUMNS](ee_rearrange_columns) | CSV 列を再配置します。 |
| [EE\_REDRAW](ee_redraw) | ウィンドウの再描画を行うかどうかを指定します |
| [EE\_REG\_SET\_VALUE](ee_reg_set_value) | EmEditorのセッティングに依存している記載か INI ファイルに値をセットします。 |
| [EE\_REG\_QUERY\_VALUE](ee_reg_query_value) | EmEditorのセッティングに依存している記載か INI ファイルからの値を問い合わせます。 |
| [EE\_RELEASE](ee_release) | プラグインの参照数を1つ減少させます。 |
| [EE\_REPLACE\_IN\_FILESA](ee_replace_in_filesa) | 指定するパスの複数のファイルから ANSI 文字列を置換します。 |
| [EE\_REPLACE\_IN\_FILESW](ee_replace_in_filesw) | 指定するパスの複数のファイルから Unicode 文字列を置換します。 |
| [EE\_REPLACEA](ee_replacea) | ANSI 文字列を置換します。 |
| [EE\_REPLACEW](ee_replacew) | Unicode文字列を置換します。 |
| [EE\_RUN\_MACRO](ee_run_macro) | マクロを起動します。 |
| [EE\_SAVE\_FILEA](ee_save_filea) | 文書を指定するファイルに保存します (ANSI)。 |
| [EE\_SAVE\_FILEW](ee_save_filew) | 文書を指定するファイルに保存します (Unicode)。 |
| [EE\_SERIAL\_TO\_LOGICAL](ee_serial_to_logical) | シリアル位置を論理座標に変換します。 |
| [EE\_SET\_ANCHOR\_POS](ee_set_anchor_pos) | 選択範囲の開始位置を設定します。 |
| [EE\_SET\_CARET\_POS](ee_set_caret_pos) | カーソル位置を移動し、選択範囲を伸縮することもできます。 |
| [EE\_SET\_CELL](ee_set_cell) | CSV モードで指定するセルに文字列を設定します。 |
| [EE\_SET\_COLUMN](ee_set_column) | CSV モードで指定する列に文字列を設定または挿入します。 |
| [EE\_SET\_CONFIGA](ee_set_configa) | 選択されている設定の名前をANSI文字列で設定します。 |
| [EE\_SET\_CONFIGW](ee_set_configw) | 選択されている設定の名前をUnicode文字列で取得します。 |
| [EE\_SET\_MODIFIED](ee_set_modified) | 文書が更新されているかどうかのフラグを設定します。 |
| [EE\_SET\_MULTI\_SEL](ee_set_multi_sel) | 複数選択が利用可能な場合、指定する選択の情報を設定します。 |
| [EE\_SET\_OUTLINE\_ARRAY](ee_set_outline_array) | 指定する複数行のアウトラインのレベルを設定します。 |
| [EE\_SET\_OUTLINE\_LEVEL](ee_set_outline_level) | 指定する論理行のアウトラインのレベルを設定します。 |
| [EE\_SET\_SCROLL\_POS](ee_set_scroll_pos) | スクロール バーの位置を設定します。 |
| [EE\_SET\_SEL\_LENGTH](ee_set_sel_length) | 選択テキストの長さを設定します。 |
| [EE\_SET\_SEL\_TYPE](ee_set_sel_type) | 選択状態の種類を設定します。 |
| [EE\_SET\_SEL\_VIEW](ee_set_sel_view) | 選択テキストの開始位置と終了位置を設定します。 |
| [EE\_SET\_STATUSA](ee_set_statusa) | ステータス メッセージにANSI文字列を設定します。 |
| [EE\_SET\_STATUSW](ee_set_statusw) | ステータス メッセージにUnicode文字列を設定します。 |
| [EE\_SHOW\_OUTLINE](ee_show_outline) | アウトラインを表示または非表示に設定します。 |
| [EE\_SHOW\_TIP](ee_show_tip) | ツールチップの表示/非表示を切り替えます。 |
| [EE\_SPLIT\_COLUMN](ee_split_column) | 現在の CSV 文書の指定された列を分割します。 |
| [EE\_TOOLBAR\_CLOSE](ee_toolbar_close) | カスタム ツール バーを閉じます。 |
| [EE\_TOOLBAR\_OPEN](ee_toolbar_open) | カスタム ツール バーを開きます。 |
| [EE\_TOOLBAR\_SHOW](ee_toolbar_show) | カスタム ツール バーの表示/非表示を切り替えます。 |
| [EE\_UNPIVOT](ee_unpivot) | CSV データを平らにして行に変換します。 |
| [EE\_UPDATE\_TOOLBAR](ee_update_toolbar) | 指定するコマンドIDのツール バーの状態を更新します。 |
| [EE\_VIEW\_TO\_DEV](ee_view_to_dev) | 表示座標をデバイス座標 (クライアント座標) に変換します。 |
| [EE\_VIEW\_TO\_LOGICAL](ee_view_to_logical) | 表示座標を論理座標に変換します。 |

これらの定数は、ヘッダ (plugin.h) で定義されています。

次の Windows API メッセージもサポートしています。一部のメッセージについては完全にサポートしているわけではありません。ウィンドウ ハンドルには、EmEditor のフレームではなく、ビューを指定します。詳しくは、SDK のリファレンスをお読みください。これらのメッセージについて詳しくは、Microsoft MSDN ライブラリを参考にしてください。

|     |     |
| --- | --- |
| EM\_GETSEL | 選択範囲の開始位置と終了位置を取得します |
| EM\_SCROLLCARET | カーソル位置にスクロールします |
| EM\_SETSEL | 選択範囲の開始位置と終了位置を設定します |
| EM\_REPLACESEL | 選択テキストを置き換えます |
| WM\_CLEAR | 選択範囲を削除します |
| WM\_COPY | 選択範囲をクリップ ボードにコピーします |
| WM\_CUT | 選択範囲を切り取ってクリップ ボードにコピーします |
| WM\_GETTEXT | 文書全体を取得します |
| WM\_GETTEXTLENGTH | 文書全体を取得するのに必要な終端ヌル文字を除く文字数を取得します |
| WM\_PASTE | クリップ ボードの中身をカーソル位置に貼り付けます |
| WM\_SETTEXT | 文書全体を設定します |
| WM\_UNDO | 最後の操作を元に戻します |


```{toctree}
:maxdepth: 1
:hidden:
ee_add_ref
ee_autofill
ee_clip_history
ee_compare
ee_convert
ee_convert_csv
ee_convert_ex
ee_custom_bar_close
ee_custom_bar_open
ee_dev_to_view
ee_do_idle
ee_edit_column
ee_edit_temp
ee_empty_undo_buffer
ee_enum_config
ee_enum_highlight
ee_exec_command
ee_exec_plugin
ee_extract_frequent
ee_filter
ee_find_in_filesa
ee_find_in_filesw
ee_find_regex
ee_find_replace
ee_finda
ee_findw
ee_free
ee_get_accel_array
ee_get_active_string
ee_get_anchor_pos
ee_get_attr
ee_get_caret_pos
ee_get_cell
ee_get_cmd_id
ee_get_color
ee_get_column
ee_get_configa
ee_get_configw
ee_get_dropped_file
ee_get_filter
ee_get_linea
ee_get_lines
ee_get_linew
ee_get_margin
ee_get_modified
ee_get_multi_sel
ee_get_outline_level
ee_get_output_string
ee_get_page_size
ee_get_redraw
ee_get_ref
ee_get_scroll_pos
ee_get_sel_end
ee_get_sel_start
ee_get_sel_texta
ee_get_sel_textw
ee_get_sel_type
ee_get_statusa
ee_get_statusw
ee_get_unicode_name
ee_get_version
ee_get_word
ee_help
ee_info
ee_info_ex
ee_insert_filea
ee_insert_filew
ee_insert_stringa
ee_insert_stringw
ee_is_char_half_or_full
ee_join
ee_keyboard_prop
ee_line_from_char
ee_line_index
ee_load_configa
ee_load_configw
ee_load_filea
ee_load_filew
ee_logical_to_serial
ee_logical_to_view
ee_manage_duplicates
ee_match_regex
ee_numbering
ee_output_dir
ee_output_string
ee_pivot_table
ee_query_status
ee_query_string
ee_query_string_ex
ee_rearrange_columns
ee_redraw
ee_reg_query_value
ee_reg_set_value
ee_release
ee_replace_in_filesa
ee_replace_in_filesw
ee_replacea
ee_replacew
ee_run_macro
ee_save_filea
ee_save_filew
ee_serial_to_logical
ee_set_anchor_pos
ee_set_caret_pos
ee_set_cell
ee_set_column
ee_set_configa
ee_set_configw
ee_set_modified
ee_set_multi_sel
ee_set_outline_array
ee_set_outline_level
ee_set_scroll_pos
ee_set_sel_length
ee_set_sel_type
ee_set_sel_view
ee_set_statusa
ee_set_statusw
ee_show_outline
ee_show_tip
ee_sort
ee_split_column
ee_toolbar_close
ee_toolbar_open
ee_toolbar_show
ee_unpivot
ee_update_toolbar
ee_view_to_dev
ee_view_to_logical
```
