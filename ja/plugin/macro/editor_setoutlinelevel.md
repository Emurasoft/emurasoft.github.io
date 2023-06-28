# Editor\_SetOutlineLevel

指定する論理行のアウトラインのレベルを設定します。このインライン関数を使うか、または
[EE\_SET\_OUTLINE\_LEVEL](../message/ee_set_outline_level) メッセージを直接送ることができます。

Editor\_SetOutlineLevel( HWND hwnd, INT\_PTR nLogicalLine, int
nLevel );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nLogicalLine_

> アウトラインのレベルを設定したい論理行を指定します。

_nLevel_

> アウトラインのレベルを指定します。

## 戻り値

> 戻り値は利用されません。

## バージョン

> Version 6.00 以上で利用できます。