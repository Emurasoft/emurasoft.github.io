# Editor\_ToolbarShow

カスタム ツール バーの表示/非表示を切り替えます。このインライン関数を直接送るか、または [EE\_TOOLBAR\_SHOW メッセージ](../message/ee_toolbar_show) を使うことができます。

Editor\_ToolbarShow( HWND hwnd, UINT nCustomRebarID, BOOL bVisible );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nToolbarID_

閉じるツール バーを指定します。EE\_TOOLBAR\_OPEN メッセージからの戻り値になります。

_bVisible_

TRUE を指定するとツール バーが表示され、FALSE を指定するとツール バーが非表示になります。

## 戻り値

メッセージが成功し、かつツール バーの状態が変更されたら TRUE を返します。失敗するか変更がなければ FALSE を返します。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
