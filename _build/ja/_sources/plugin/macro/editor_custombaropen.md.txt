# Editor\_CustomBarOpen

カスタム バーを開きます。このメッセージを送る前に、既に、別のカスタム バーが開いている場合は、そのカスタム バーを閉じて、新しいカスタム バーを開きます。このインライン関数を使うか、または [EE\_CUSTOM\_BAR\_OPEN メッセージ](../message/ee_custom_bar_open) を直接送ることができます。

Editor\_CustomBarOpen( HWND hwnd, CUSTOM\_BAR\_INFO\* pCustomBarInfo );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pCustomBarInfo_

> [CUSTOM\_BAR\_INFO 構造体](../structure/custom_bar_info) へのポインタを指定します。

## 戻り値

> 成功すると、カスタム バー ID を返します。この ID は、Editor\_CustomBarClose インライン関数で閉じるときに必要です。失敗すると 0 を返します。

## バージョン

> Version 6.00 以上で利用できます。