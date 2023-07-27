# EE\_INFO

実行中の EmEditor または指定するドキュメントに関する情報を取得または設定を行います。このメッセージを直接送るか、 [Editor\_Info](../macro/editor_info)、 [Editor\_DocInfo](../macro/editor_docinfo)、または [Editor\_DocInfoEx](../macro/editor_docinfoex) インライン関数を使うことができます。

EE\_INFO

wParam = (WPARAM)nCmd;

lParam = (LPARAM)lParam;

または

EE\_INFO

wParam = MAKEWPARAM(nCmd, iDoc+1);

lParam = (LPARAM)lParam;

## パラメータ

_nCmd_

取得または設定する情報の種類を指定します。次のうちのいずれかとなります。

| nCmd | 意味 | lParam | 戻り値 |
| --- | --- | --- | --- |
| EI\_GET\_ENCODE | 次に保存する時に使用される文字コードを取得します。 | 使用されません。 | (int)nCP<br> 文字コード |
| EI\_SET\_ENCODE | 次に保存する時に使用される文字コードを設定します。 | (UINT)nCP<br> CODEPAGE\_ で始まる文字コードを指定します。 | 使用されません。 |
| EI\_GET\_SIGNATURE | 次に保存する時にUnicode, UTF-8の署名を付けるかどうかを取得します。 | 使用されません。 | (BOOL)bSignature<br> TRUE なら署名を付けます。 |
| EI\_SET\_SIGNATURE | 次に保存する時にUnicode, UTF-8の署名を付けるかどうかを設定します。 | (BOOL)bSignature<br> TRUEなら署名を付けます。 | 使用されません。 |
| EI\_GET\_FONT\_CHARSET | フォントの文字セットを取得します。 | 使用されません。 | (int)nCharset<br> 文字セットを返します。 |
| EI\_SET\_FONT\_CHARSET | フォントの文字セットを設定します。 | (int)nCharset<br> CHARSET\_ で始まる文字セットを指定します。 | 使用されません。 |
| EI\_GET\_FONT\_CP | 表示されているフォントのコードページを取得します。 | 使用されません。 | (UINT)nCP<br> コードページ。 |
| EI\_GET\_INPUT\_CP | 入力言語に対応するコードページを取得します。 | 使用されません。 | (UINT)nCP<br> コードページ。 |
| EI\_GET\_SHOW\_TAG | タグを下線表示するかどうかを取得します。 | 使用されません。 | (BOOL)bShowTag<br> TRUEならタグを下線表示します。 |
| EI\_SET\_SHOW\_TAG | タグを下線表示するかどうかを設定します。 | (BOOL)bShowTag<br> TRUEならタグを下線表示します。 | 使用されません。 |
| EI\_GET\_FILE\_NAMEA | 開いているファイル名をANSI文字列で取得します。 | (LPSTR)szFileName<br> ファイル名を取得するバッファへのポインタを指定します。バッファには、NULL文字を含めてMAX\_PATHバイトを確保しておく必要があります。 | 使用されません。 |
| EI\_GET\_FILE\_NAME\_EX | 開いているファイル名をUnicode文字列で取得します。 | (STRING\_BUF\*)pStringBuf<br> ファイル名を取得するための [STRING\_BUF 構造体](../structure/string_buf) へのポインタを指定します。 | 使用されません。 |
| EI\_GET\_FILE\_NAMEW | 開いているファイル名をUnicode文字列で取得します。 | (LPWSTR)szFileName<br> ファイル名を取得するバッファへのポインタを指定します。バッファには、NULL文字を含めてMAX\_PATH文字分を確保しておく必要があります。 | 使用されません。 |
| EI\_SET\_FILE\_NAMEW | 現在開いているファイル名をリネームします。文書が無題の場合、ファイルを保存しないで文書のタイトルを変更します。 | (LPCWSTR)pszName<br>新しい名前を指定します。 | (HRESULT)hr<br>失敗すると負の値を返します。 |
| EI\_IS\_PROPORTIONAL\_FONT | 表示フォントがプロポーショナル フォントかどうかを取得します。Windows XP/2003 では、常に TRUE を返します。 | 使用されません。 | (BOOL)bProportionalFont<br> プロポーショナル フォントなら TRUE を、固定幅なら FALSE を返します。 |
| EI\_GET\_NEXT\_BOOKMARK | 次のブックマーク位置を取得します。 | (INT\_PTR)yLine<br> 検索を開始する論理行を指定します。-1 を指定すると、文書の先頭から検索を始めます。 | (INT\_PTR)yLine<br> 検索したブックマークの論理行を返します。見つからない場合は -1 を返します。 |
| EI\_GET\_HILITE\_FIND | 検索文字列を強調表示するかどうかを取得します。 | 使用されません。 | (BOOL)bShowFindHilite |
| EI\_SET\_HILITE\_FIND | 検索文字列を強調表示するかどうかを設定します。 | (BOOL)bShowFindHilite | 使用されません。 |
| EI\_GET\_APP\_VERSIONA | バージョン名をANSI文字列で取得します。 | (LPSTR)szVersionName<br> バージョン名を取得するバッファへのポインタを指定します。バッファには、NULL文字を含めてMAX\_PATHバイトを確保しておく必要があります。 | 使用されません。 |
| EI\_GET\_APP\_VERSIONW | バージョン名をUnicode文字列で取得します。 | (LPWSTR)szVersionName<br> バージョン名を取得するバッファへのポインタを指定します。バッファには、NULL文字を含めてMAX\_PATH文字分を確保しておく必要があります。 | 使用されません。 |
| EI\_GET\_READ\_ONLY | 書き換え禁止状態かどうかを取得します。 | 使用されません。 | (BOOL)bReadOnly |
| EI\_IS\_WINDOW\_COMBINED | ウィンドウが結合された状態かどうかを取得します。 | 使用されません。 | (BOOL)bCombined |
| EI\_WINDOW\_COMBINE | ウィンドウの結合状態を設定します。 | (BOOL)bCombined<br> TRUEなら結合します。FALSEなら結合を解除します。 | 使用されません。 |
| EI\_IS\_UNDO\_COMBINED | TRUE だと挿入文字列を一度に元に戻します。FALSE だと文字単位で元に戻します。 | 使用されません。 | (BOOL)bCombined |
| EI\_GET\_DOC\_COUNT | 現在のフレーム ウィンドウに開かれているドキュメントの数を返します。 (EmEditor Professional 5.00 以上のみ) | 使用されません。 | (int)nCount<br> ドキュメントの数を返します。 |
| EI\_INDEX\_TO\_DOC | ドキュメントのインデックスからハンドルに変換します。 (EmEditor Professional 5.00 以上のみ) | ドキュメントの 0 を基底とするインデックスを指定します。 | (HEEDOC)hDoc<br> ドキュメントへのハンドルを返します。 |
| EI\_DOC\_TO\_INDEX | ドキュメントのハンドルからインデックスに変換します。 | ドキュメントへのハンドルを指定します。 | (int)nIndex<br> ドキュメントの 0 を基底とするインデックスを返します。 |
| EI\_ZORDER\_TO\_DOC | ドキュメントの Z オーダーからハンドルに変換します。 | ドキュメントの 0 を基底とするZオーダーを指定します。 | (HEEDOC)hDoc<br> ドキュメントへのハンドルを返します。 |
| EI\_DOC\_TO\_ZORDER | ドキュメントのハンドルから Z オーダーに変換します。 | ドキュメントへのハンドルを指定します。 | (int)nZOrder<br> ドキュメントの 0 を基底とする Z オーダーを返します。 |
| EI\_GET\_ACTIVE\_INDEX | アクティブなドキュメントのインデックスを取得します。 | 使用されません。 | (int)nIndex<br> ドキュメントの 0 を基底とするインデックスを返します。 |
| EI\_SET\_ACTIVE\_INDEX | ドキュメントをアクティブにします。 | 使用されません。 | (BOOL)bSuccess<br> 成功すると TRUE を、失敗すると FALSE を返します。 |
| EI\_GET\_FULL\_TITLEA | ドキュメントの長いタイトルを ANSI 文字列で取得します。 | (LPSTR)szＴｉｔｌｅ<br> タイトルを取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH バイトを確保しておく必要があります。 | 使用されません。 |
| EI\_GET\_FULL\_TITLEW | ドキュメントの長いタイトルを Unicode 文字列で取得します。 | (LPWSTR)szTitle<br> タイトルを取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH 文字分を確保しておく必要があります。 | 使用されません。 |
| EI\_GET\_SHORT\_TITLEA | ドキュメントの短いタイトルを ANSI 文字列で取得します。 | (LPSTR)szＴｉｔｌｅ<br> タイトルを取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH バイトを確保しておく必要があります。 | 使用されません。 |
| EI\_GET\_SHORT\_TITLEW | ドキュメントの短いタイトルを Unicode 文字列で取得します。 | (LPWSTR)szTitle<br> タイトルを取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH 文字分を確保しておく必要があります。 | 使用されません。 |
| EI\_GET\_SAVE\_AS\_TITLEA | ドキュメントの長いタイトルからファイルが変更されたかどうかを示すアスタリスク「\*」を除いた文字列を ANSI 文字列で取得します。 | (LPSTR)szＴｉｔｌｅ<br> タイトルを取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH バイトを確保しておく必要があります。 | 使用されません。 |
| EI\_GET\_SAVE\_AS\_TITLEW | ドキュメントの長いタイトルからファイルが変更されたかどうかを示すアスタリスク「\*」を除いた文字列を Unicode 文字列で取得します。 | (LPWSTR)szTitle<br> タイトルを取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH 文字分を確保しておく必要があります。 | 使用されません。 |
| EI\_MOVE\_ORDER | ドキュメントのタブの順番を変更します。 | 移動先のTabの位置を 0 を基底とするインデックスで指定します。 | 使用されません。 |
| EI\_CLOSE\_DOC | ドキュメントを閉じます。 | 使用されません。 | (BOOL)bSuccess<br> 成功すると TRUE を、失敗すると FALSE を返します。 |
| EI\_SAVE\_DOC | ドキュメントを保存します。無題の場合は「名前を付けて保存」ダイアログ ボックスが表示されます。 | 使用されません。 | (BOOL)bSuccess<br> 成功すると TRUE を、失敗すると FALSE を返します。無題の場合に「名前を付けて保存」ダイアログ ボックスで \[キャンセル\] を選択すると、FALSE を返します。 |
| EI\_GET\_CURRENT\_FOLDER | 現在の作業フォルダを取得します。 | (LPWSTR)szDir<br> フォルダ名を取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH 文字分を確保しておく必要があります。 | 使用されません。 |
| EI\_IS\_LARGE\_DOC | 非常に大きなファイルかどうかを取得します。 | 使用されません。 | (BOOL)bLarge<br> 非常に大きなファイルの場合は TRUE を、そうでなければ FALSE を返します。 |
| EI\_USE\_INI | INI ファイルがレジストリの代わりに使用されているかどうかを取得します。 | 使用されません。 | (BOOL)bIni<br> INI ファイルが使用されている場合は TRUE を、レジストリが使用されている場合は FALSE を返します。 |
| EI\_GET\_LANGUAGE | 現在選択されているユーザー インターフェイス用の言語を取得します。 | (LPWSTR)szFolder<br> 言語フォルダを取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH 文字分を確保しておく必要があります。 | (UINT)nLangID<br> 現在選択されている言語 ID を返します。 |
| EI\_COMBINE\_HISTORY | 元に戻す履歴の1つとして、次の変更を前の変更と結合するかどうかを指定します。 | (BOOL)bCombine<br> 結合する場合は TRUE を返します | 使用されません。 |
| EI\_GET\_BAR\_TEXT\_COLOR | カスタム バーの文字色を取得します。 | 使用されません。 | (COLORREF)clrText<br> 文字色の RGB 値。 |
| EI\_GET\_BAR\_BACK\_COLOR | カスタム バーの背景色を取得します。 | 使用されません。 | (COLORREF)clrBack<br> 背景色の RGB 値。 |
| EI\_GET\_RETURN\_TYPE | 現在行の改行コードを取得します。現在行が文書の最終行で改行コードを持たない場合、1つ前の行の改行コードを取得します。 | (UINT\_PTR)yLogicalLine<br> 論理行を指定します。 | (int)nReturnType<br> RETURN\_METHOD\_BOTH、RETURN\_METHOD\_CR\_ONLY、RETURN\_METHOD\_LF\_ONLY のいずれかを返します。 |
| EI\_GET\_ACTIVE\_DOC | アクティブなドキュメントへのハンドルを取得します。 | 使用されません。 | (HEEDOC)hDoc<br> アクティブにするドキュメントへのハンドルを返します。 |
| EI\_SET\_ACTIVE\_DOC | ドキュメントをアクティブにします。 | (HEEDOC)hDoc<br> アクティブにするドキュメントへのハンドルを指定します。 | (BOOL)bSuccess<br>成功すると TRUE を、失敗すると FALSE を返します。 |
| EI\_GET\_SYNC\_SESSION | ドキュメントが比較または同期スクロールモードの場合、ドキュメントのセッションIDを取得します。 | 使用されません。 | (int)nSessionID<br> ドキュメントが比較または同期スクロールモードの場合、ドキュメントのセッションIDを返します。ドキュメントが通常モードの場合、0 を返します。 |
| EI\_GET\_LOC\_DLL\_INSTANCE | ローカライズされたリソース DLL のインスタンスを返します。 | 使用されません。 | (HINSTANCE)hinstLoc<br>ローカライズされたリソース DLL のインスタンスを返します。 |
| EI\_GET\_RES\_DLL\_INSTANCE | リソース DLL のインスタンスを返します。 | 使用されません。 | (HINSTANCE)hinstRes<br>リソース DLL のインスタンスを返します。 |
| EI\_GET\_CMD\_LIST\_SIZE | 指定する複数メニュー コマンドで利用可能な項目数を返します。 | 使用されません。 | (int)nCount<br>利用可能な項目数を返します。 |
| EI\_GET\_DISCARD\_UNDO | EmEditor が置換、挿入、削除の速度を改善するために元に戻す情報を破棄するかどうかを示すフラグを取得します。 | 使用されません。 | (BOOL)bDiscardUndo<br>フラグを返します。 |
| EI\_SET\_DISCARD\_UNDO | EmEditor が置換、挿入、削除の速度を改善するために元に戻す情報を破棄するかどうかを示すフラグを設定します。 | (BOOL)bDiscardUndo<br>フラグ。 | 使用されません。 |
| EI\_GET\_HEADING\_LINES | ヘディング (非スクロール領域) の行数を取得します。 | 使用されません。 | (int)nHeadingLines |
| EI\_SET\_HEADING\_LINES | ヘディング (非スクロール領域) の行数を設定します。 | (int)nHeadingLines | 使用されません。 |
| EI\_GET\_NARROWING\_TOP | 部分編集の最上部の位置 (Y 座標) を取得します。-1 は、部分編集が設定されていないことを意味します。 | 使用されません。 | (int)nNarrowingTop |
| EI\_SET\_NARROWING\_TOP | 部分編集の最上部の位置 (Y 座標) を設定します。-1 は、部分編集が設定されていないことを意味します。 | (int)nNarrowingTop | 使用されません。 |
| EI\_GET\_NARROWING\_BOTTOM | 部分編集の最下部の位置 (Y 座標) を取得します。-1 は、部分編集が設定されていないことを意味します。 | 使用されません。 | (int)nNarrowingBottom |
| EI\_SET\_NARROWING\_BOTTOM | 部分編集の最下部の位置 (Y 座標) を設定します。-1 は、部分編集が設定されていないことを意味します。 | (int)nNarrowingBottom | 使用されません。 |
| EI\_SET\_HILITE\_FILTER | 最後に使った検索の情報を使ってフィルターを設定します。アクティブなドキュメントのみ使用できます。 | 使用されません。 | 使用されません。 |
| EI\_GET\_CSV | 現在の CSV モードのインデックスを取得します。CSV モードでない場合は -1 を返します。 | 使用されません。 | (int)iCSV |
| EI\_GET\_PRINT\_PAGES | 現在選択されているプリンター用のページ数を取得します。アクティブなドキュメントのみ使用できます。 | (BOOL)bSelOnly<br>選択範囲のみを使用してページ数を計算するかどうかを指定します。 | (int)nPages |
| EI\_GET\_CELL\_MODE | CSV セル選択モードかどうかを示すフラグを取得します。 | 使用されません。 | (BOOL)bCellMode |
| EI\_SET\_CELL\_MODE | CSV セル選択モードかどうかを示すフラグを設定します。 | (BOOL)bCellMode | 使用されません。 |
| EI\_GET\_UNTITLED | 文書が無題かどうかを示すフラグを取得します。 | 使用されません。 | (BOOL)bUntitled |
| EI\_GET\_DPI | 現在のモニターの DPI 値を取得します。 | 使用されません。 | (long)nDPI |
| EI\_GET\_FILTER\_VISIBLE\_LINES\_ABOVE | フィルターで一致した行の上に表示する行数を取得します。 | 使用されません。 | (long)nLines |
| EI\_SET\_FILTER\_VISIBLE\_LINES\_ABOVE | フィルターで一致した行の上に表示する行数の設定します。 | (long)nLines | 使用されません。 |
| EI\_GET\_FILTER\_VISIBLE\_LINES\_BELOW | フィルターで一致した行の下に表示する行数を取得します。 | 使用されません。 | (long)nLines |
| EI\_SET\_FILTER\_VISIBLE\_LINES\_BELOW | フィルターで一致した行の下に表示する行数の設定します。 | (long)nLines | 使用されません。 |
| EI\_GET\_DPI\_OPTIONS | モニターに関するオプションを取得します。現在のところ、DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED のみがサポートされています。DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED が設定されていると、DPI の変更に応じてウィンドウのサイズが変更されます。 | 使用されません。 | (long)nFlags |
| EI\_SET\_DPI\_OPTIONS | モニターに関するオプションを設定します。現在のところ、DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED のみがサポートされています。DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED が設定されていると、DPI の変更に応じてウィンドウのサイズが変更されます。 | (long)nFlags | 使用されません。 |
| EI\_GET\_REGISTERED\_NAME | \[バージョン情報\] ダイアログ ボックスに表示される、ユーザー登録されている名前を取得します。製品が登録されていない場合、空の文字列が取得されます。 | (LPWSTR)szName<br>文字列を取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_REG\_NAME 文字分を確保しておく必要があります。 | 使用されません。 |
| EI\_VALIDATE\_CSV | CSV文書の正当性を確認してエラーを出力し、オプションにより区切り位置を調節します。 | (int)nFlags<br>次の値の組み合わせを指定します。<br>VALIDATE\_ADJUST\_COLUMNS, VALIDATE\_QUIET, VALIDATE\_ADJUST\_VISIBLE\_ONLY, VALIDATE\_DETECT\_NL, VALIDATE\_QUIET\_IF\_NO\_ERROR, VALIDATE\_ADJUST\_ENLARGE\_ONLY,  VALIDATE\_DETECT\_CSV,  VALIDATE\_ASYNC | (int)nResults<br>戻り値は、次の値の組み合わせになります。戻り値が 0 の場合エラーが無いことを意味します。<br>CSV\_ADJUSTED, CSV\_NL\_EMBEDDED, CSV\_ABORT, CSV\_INVALID\_QUOTES, CSV\_INCONSISTENT\_COLUMNS, CSV\_NOT\_CSV, CSV\_ASYNC\_SUCCESS,  CSV\_ASYNC\_RUNNING |
| EI\_GET\_CLIENT\_RECT\_NO\_BARS | スクロール バーまたはミニマップに占有された領域を除くエディタ ビューの座標を取得します。 | (RECT\*)pRect | 成功すると TRUE を、失敗すると FALSE を返します。 |
| EI\_REFRESH\_COMMON\_SETTINGS | 共通の設定をロードし EmEditor ウィンドウを最新の情報に更新します。 | 使用されません。 | 使用されません。 |
| EI\_GET\_NEWLINE\_CODE | 文書で使用された改行コードを取得します。 | 使用されません。 | FLAG\_CR\_AND\_LF、FLAG\_CR\_ONLY、FLAG\_LF\_ONLY、または FLAG\_NEWLINE\_MIXED を返します。 |
| EI\_GET\_MEMORY\_SIZE | 文書で使用されている1かたまりのメモリ サイズを取得します。既定値は、\[カスタマイズ\] ダイアログ ボックスの [\[高度\] ページ](../../dlg/advanced/index) の \[メモリ サイズ\] テキスト ボックスで指定された値になります。 | 使用されません。 | メモリ サイズを返します。 |
| EI\_SET\_MEMORY\_SIZE | 文書で使用される1かたまりのメモリ サイズを設定します。既定値は、\[カスタマイズ\] ダイアログ ボックスの [\[高度\] ページ](../../dlg/advanced/index) の \[メモリ サイズ\] テキスト ボックスで指定された値になります。 | (long)nBits<br>必要なメモリ サイズを指定します。 | 新しいメモリ サイズを返します。文書がすでにより多くのメモリ サイズを使用している場合、この値は指定されたサイズよりも大きくなることがあります。 |
| EI\_GET\_BOOKMARK\_COUNT | 文書内のブックマークの数を取得します。 | 使用されません。 | 文書内のブックマークの数を返します。 |
| EI\_SYNC\_NOW | EmEditorをトリガーして、今すぐ同期します。 | (UINT)nFlags<br>次の値の組み合わせを指定します。<br>SYNC\_FLAG\_SEND, SYNC\_FLAG\_RECEIVE, SYNC\_FLAG\_FORCE, and SYNC\_FLAG\_REFRESH\_UI. | 使用されません。 |
| EI\_GET\_CHAR\_TYPE | 文字のタイプを取得します。 | (LPCWSTR)pch | 文字のタイプを返します。次のタイプのいずれかを指定できます。<br>CHAR\_NULL, CHAR\_SPACE, CHAR\_MARK, CHAR\_ALPHANUMERIC, CHAR\_KANA , CHAR\_KANA\_MARK , CHAR\_DB\_SPACE, CHAR\_DB\_MARK, CHAR\_DB\_ALPHANUMERIC, CHAR\_DB\_HIRA, CHAR\_DB\_KATA, CHAR\_DB\_KANJI, CHAR\_DB\_KANA\_MARK, CHAR\_SECOND\_DB, CHAR\_HANGUL, CHAR\_DB\_HANGUL |
| EI\_FILE\_POS\_TO\_LOGICAL | ファイル位置を論理位置に変換します。 | (FILE\_POS\_INFO\*)pFilePosInfo | 使用されません。 |
| EI\_LOGICAL\_TO\_FILE\_POS | 論理位置をファイル位置に変換します。 | (FILE\_POS\_INFO\*)pFilePosInfo | 使用されません。 |
| EI\_CELL\_TO\_LOGICAL | セル位置を論理位置に変換します。 | (CELL\_LOGICAL\_INFO\*)pCellLogicalInfo | 使用されません。 |
| EI\_LOGICAL\_TO\_CELL | 論理位置をセル位置に変換します。 | (CELL\_LOGICAL\_INFO\*)pCellLogicalInfo | 使用されません。 |
| EI\_IS\_VERY\_DARK | システムでダーク モードがサポートされているか調べ、サポートされている場合、ユーザーが非常に暗いモードを選択しているかを調べます。 | 使用されません。 | ユーザーが非常に暗いモードを選択していると TRUE を返し、そうでない場合 FALSE を返します。ただし、システムでダーク モードがサポートされていない場合は NOT\_SUPPORTED を返します。 |
| EI\_WM\_INITDIALOG | 非常に暗いモードをサポートするために、ダイアログ プロシージャーの WM\_INITDIALOG メッセージの中で呼ばれます。 | (HWND)hWnd | 使用されません。 |
| EI\_WM\_CTLCOLOR | 非常に暗いモードをサポートするために、ダイアログ プロシージャーの WM\_CTLCOLORDLG、WM\_CTLCOLORSTATIC、WM\_CTLCOLOREDIT、WM\_CTLCOLORBTN、WM\_CTLCOLORLISTBOX メッセージの中で呼ばれます。 | (WPARAM)wParam<br>WM\_CTLCOLORxxx メッセージの wParam を渡すことができます。 | 非常に暗いモードが選択されている場合、ブラシを返します。この値をダイアログ プロシージャーの戻り値に渡す必要があります。 |
| EI\_WM\_THEMECHANGED | 非常に暗いモードをサポートするために、ダイアログ プロシージャーの WM\_THEMECHANGED メッセージの中で呼ばれます。 | (HWND)hWnd | 使用されません。 |
| EI\_INIT\_LISTVIEW | 非常に暗いモードをサポートするために、リストビュー コントロールを初期化します。 | (HWND)hWnd | 使用されません。 |
| EI\_GET\_VIEW\_FONT | 現在、選択されているエディタ フォントへのハンドルを取得します。 | 使用されません。 | (HFONT)hFont |
| EI\_GET\_HIDE\_QUOTES | CSV セル選択モードで \[引用符で囲まないで/エスケープしないで表示\] が有効かどうかを示すフラグを取得します。 | 使用されません。 | (BOOL)bHideQuotes |
| EI\_SET\_HIDE\_QUOTES | CSV セル選択モードで \[引用符で囲まないで/エスケープしないで表示\] が有効かどうかを示すフラグを設定します。 | (BOOL)bHideQuotes | 使用されません。 |
| EI\_ENABLE\_WM\_CHAR | 内部で使用されます。 | 使用されません。 | 内部で使用されます。 |
| EI\_GET\_SYNC | 同期フォルダへのパスを取得します。 | (LPWSTR)szDir<br>フォルダ名を取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_PATH 文字分を確保しておく必要があります。 | SYNC\_SETTINGS\_SEND, SYNC\_SETTINGS\_RECEIVE を含む値の組み合わせを返します。 |
| EI\_GET\_SPLIT | 分割の状態を取得します。 | 使用されません。 | 次の値のどれかを返します:<br>SPLIT\_NONE, SPLIT\_HORZ, SPLIT\_VERT, SPLIT\_BOTH, SPLIT\_2\_HORZ, SPLIT\_2\_VERT |
| EI\_GET\_SUM | 選択範囲に含まれる数の合計と出現数を取得します。 | (SUM\_INFO\*)pSumInfo | 成功すると TRUE を、失敗すると FALSE を返します。 |
| EI\_GET\_CONFIG | 選択されている設定の名前を取得します。 | 設定の名前を取得するバッファへのポインタを指定します。バッファには、NULL 文字を含めて MAX\_CONFIG\_NAME 文字分を確保しておく必要があります。 | 使用されません。 |
| EI\_SET\_CONFIG | 指定する設定に変更します。 | 設定の名前を指定します。 | (BOOL)bSuccess |
| EI\_SAVE\_FILE | 文書を保存します。 | 完全パスのファイル名を指定します。 | (BOOL)bSuccess |
| EI\_INDEX\_TO\_DOC\_REAL | ドキュメントのインデックスからハンドルに変換します。EI\_INDEX\_TO\_DOC と異なり、このコマンドは分割ウィンドウ内の個々の文書を数えます。 | ドキュメントの 0 を基底とするインデックスを指定します。 | (HEEDOC)hDoc<br>ドキュメントへのハンドルを返します。 |
| EI\_DOC\_TO\_INDEX\_REAL | ドキュメントのハンドルからインデックスに変換します。EI\_INDEX\_TO\_DOC と異なり、このコマンドは分割ウィンドウ内の個々の文書を数えます。 | ドキュメントへのハンドルを指定します。 | (int)nIndex<br>ドキュメントの 0 を基底とするインデックスを返します。 |
| EI\_GET\_TITLE | 現在の文書のタイトルを取得します。 | (STRING\_BUF\*)pStringBuf<br> タイトルを取得するための [STRING\_BUF 構造体](../structure/string_buf) へのポインタを指定します。 | 使用されません。 |
| EI\_SET\_TITLE | 現在の文書のタイトルを設定します。タイトルには長いタイトルと短いタイトルを LF (\\n) で区切って指定することができます。 | (LPCWSTR)pszTitle<br>新しいタイトルを指定します。 | (HRESULT)hr<br>失敗すると負の値を返します。 |

_iDoc_

操作対象のドキュメントのインデックスを指定します。wParamの上位ワードには、1 を基底とするインデックスを指定します。 wParam の上位ワードに 0 を指定すると、現在アクティブなドキュメントが操作対象になります。nCmd によっては、使用されないこともあります。その場合は、wParam の上位ワードに 0 を指定する必要があります。

_lParam_

nCmd によって意味が異なります。

## 戻り値

nCmd によって意味が異なります。

## バージョン

Version 3.00 以上で利用できます。ただし、iDoc パラメータは Version 5.00 以上で利用できます。
