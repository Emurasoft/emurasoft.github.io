# Editor\_ToolbarOpen

カスタム ツール バーを開きます。このインライン関数を使うか、または [EE\_TOOLBAR\_OPEN メッセージ](../message/ee_toolbar_open) を直接送ることができます。

Editor\_ToolbarOpen( HWND hwnd, TOOLBAR\_INFO\* pToolbarInfo);

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nCmdID_

[TOOLBAR\_INFO 構造体](../structure/toolbar_info) へのポインタを指定します。

## 戻り値

成功すると、カスタム ツール バー ID を返します。失敗すると 0 を返します。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
