# Editor\_ToolbarClose

カスタム ツール バーを閉じます。このインライン関数を使うか、または [EE\_TOOLBAR\_CLOSE メッセージ](../message/ee_toolbar_close) を直接送ることができます。

Editor\_ToolbarClose( HWND hwnd, UINT nCustomRebarID );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nCmdID_

閉じるツール バーを指定します。EE\_TOOLBAR\_OPEN メッセージからの戻り値になります。

## 戻り値

関数が成功し、かつツール バーの状態が変更されたら TRUE を返します。失敗するかツール バーの状態に変更がなければ FALSE を返します。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
