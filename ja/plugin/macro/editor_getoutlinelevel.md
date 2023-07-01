# Editor\_GetOutlineLevel

指定する論理行のアウトラインのレベルを取得します。このインライン関数を使うか、または
[EE\_GET\_OUTLINE\_LEVEL](../message/ee_get_outline_level) メッセージを直接送ることができます。

Editor\_GetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nLogicalLine_

> アウトラインのレベルを取得したい論理行を指定します。

## 戻り値

> 指定する論理行のアウトラインのレベルを返します。

## バージョン

> Version 6.00 以上で利用できます。
