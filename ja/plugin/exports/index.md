# エクスポートする関数

| 関数 | 説明 |
| --- | --- |
| OnCommand( HWND hwnd ) | メニューかツールバーからプラグインを選択したときに呼び出されます |
| QueryStatus( HWND hwnd, LPBOOL pbChecked ) | プラグインが実行可能か、またはチェックされた状態かを調べます |
| OnEvents( HWND hwnd, UINT nEvent, LPARAM lParam ) | 状態が変更されたときに [イベント](../event/index) が指定されて呼び出されます |
| GetMenuTextID() | プラグインのメニューアイテムテキストのリソースIDを取得します |
| GetStatusMessageID() | ステータスバーテキストとツールバーのツールチップ用テキストを \\n で結合した文字列のリソースIDを取得します。 |
| GetBitmapID() | ツールバーに表示されるプラグイン ボタンのビットマップのリソースIDを取得します |
| PlugInProc( HWND hwnd, UINT nMsg, WPARAM wParam, LPARAM lParam ) | [プラグインへのメッセージ](../plugin_message/index) を使って、さまざまな設定や取得を行います。 |

エクスポートする関数は、すべてのプラグインに必要です。これらのエクスポートする関数は、DEF
ファイルにこの順番どおりに定義しておく必要があります。また、コンパイルの際は、呼び出し方法として \_stdcall を選択する必要があります。詳しくは、サンプルを参考にしてください。

