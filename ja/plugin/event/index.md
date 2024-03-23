# イベント

| イベント名 | 説明 |
| --- | --- |
| EVENT\_CARET\_MOVED | カーソル位置が移動した時に呼ばれます。 |
| EVENT\_CHANGE | テキストの内容が変更された時に呼ばれます。 |
| EVENT\_CHAR | 文字が挿入された時に呼ばれます。LOWORD(lParam)は挿入された文字のUnicode文字コードを表します。 |
| EVENT\_CLOSE | EmEditorが終了する直前、またはプラグインが解放される前、またはユーザーが [\[プラグインの設定\] ダイアログ ボックス](../../dlg/plugins/index) からプラグインをアンインストールしようとした時に呼ばれます。プラグインは、このイベントを受け取ったら、ただちに使用中のリソースを解放して、プラグイン DLL ファイルが削除可能な状態にする必要があります。このイベントでは、 [OnEvents 関数](../exports/index) の第 1 引数 hwnd は、NULL になります。ただし、このイベントが呼ばれても、必ずしもプラグインが解放されるとは限りません。 |
| EVENT\_CLOSE\_FRAME | EmEditor フレーム ウィンドウが閉じられる時に呼ばれます。(EmEditor Version 5.00 以上で対応) |
| EVENT\_CONFIG\_CHANGED | 現在の設定のプロパティが変更されたときに呼ばれます。<br> アクティブな文書が変更されたときにも呼ばれます。ファイルを開いた直後は現在の設定が変わっても呼ばれません。 |
| EVENT\_CREATE | EmEditorが起動した直後、またはプラグインを追加した時に呼ばれます。LOWORD(lParam)は、プラグイン自身のコマンドIDを示します。 |
| EVENT\_CREATE\_FRAME | 新しい EmEditor フレームが作成された時に呼ばれます。タブの有効、無効が切り替えられた時でも、このイベントが呼ばれます。LOWORD(lParam) は、プラグイン自身のコマンドIDを示します。(EmEditor Version 5.00 以上で対応) |
| EVENT\_CUSTOM\_BAR\_CLOSED | カスタム バーが閉じられた後に呼ばれます。EmEditor は、カスタム バーを閉じるときに、そのクライアント ウィンドウに対して、DestroyWindow() を呼びます。lParam には、 [CUSTOM\_BAR\_CLOSE\_INFO 構造体](../structure/custom_bar_close_info) へのポインタが格納されます。(EmEditor Version 6.00 以上で対応) |
| EVENT\_CUSTOM\_BAR\_CLOSING | カスタム バーが閉じられる直前に呼ばれます。lParam には、 [CUSTOM\_BAR\_CLOSE\_INFO 構造体](../structure/custom_bar_close_info) へのポインタが格納されます。(EmEditor Version 6.00 以上で対応) |
| EVENT\_DOC\_CLOSE | ドキュメントが閉じる直前に呼ばれます。lParam には、閉じられるドキュメントへのハンドル (HEEDOC) が格納されます。 (EmEditor Version 5.00 以上で対応) |
| EVENT\_DOC\_SEL\_CHANGED | アクティブなドキュメントが変更された時に呼ばれます。(EmEditor Version 5.00 以上で対応) |
| EVENT\_DROPPED | EmEditor フレーム ウィンドウにファイルがドロップされました。 |
| EVENT\_FILE\_OPENED | ファイルを開いた直後に呼ばれます。 |
| EVENT\_IDLE | アイドル時に呼ばれます。(EmEditor Version 6.00 以上で対応) |
| EVENT\_KILL\_FOCUS | フォーカスを失った時に呼ばれます。 |
| EVENT\_MODIFIED | 更新した状態、または更新されていない状態に変わった時に呼ばれます。 |
| EVENT\_SAVING | ドキュメントが保存される直前に呼ばれます。lParam には、保存されるドキュメントへのハンドル (HEEDOC) が格納されます。 (EmEditor Version 8.00 以上で対応) |
| EVENT\_SCROLL | スクロールバーの位置が変更された時に呼ばれます。 |
| EVENT\_SEL\_CHANGED | テキストの選択状態が変更された時に呼ばれます。 |
| EVENT\_SET\_FOCUS | フォーカスを取得したときに呼ばれます。 |
| EVENT\_TAB\_MOVED | タブが移動された時に呼ばれます。 |
| EVENT\_TEMP\_SAVING | ユーザーが一時テキストを保存しようとする時に呼ばれます。プラグインがファイルの保存に責任を負います。lParam には [TEMP\_INFO 構造体](../structure/temp_info) へのポインタが格納されます。 |
| EVENT\_TOOLBAR\_CLOSED | カスタム ツール バーが閉じられた後に呼ばれます。EVENT\_CUSTOM\_BAR\_CLOSED メッセージと違い、クライアント ウィンドウに対して DestroyWindow() を呼びません。lParam には [TOOLBAR\_INFO 構造体](../structure/toolbar_info) へのポインタが格納されます。(EmEditor Version 7.00 以上で利用できます。) |
| EVENT\_TOOLBAR\_SHOW | カスタム バーの表示/非表示が切り替えられた時 (RBBS\_HIDDEN スタイルが切り替えられた時) 呼ばれます。lParam には [TOOLBAR\_INFO 構造体](../structure/toolbar_info) へのポインタが格納されます。(EmEditor Version 7.00 以上で利用できます。) |
| EVENT\_UI\_CHANGED | UI が変更された時に呼ばれます。lParam は次の値の組み合わせになります: UI\_CHANGED\_LANGUAGE、UI\_CHANGED\_TOOLBARS。 |

イベントは、EmEditor から送信されプラグインで使用されます。 [OnEvents 関数](../exports/index) の
nEvent パラメータで論理和として指定されます。

これらの定数は、ヘッダ (plugin.h) で定義されています。

