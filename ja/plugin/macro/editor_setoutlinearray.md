# Editor\_SetOutlineArray

指定する複数行のアウトラインのレベルを設定します。このインライン関数を使うか、または
[EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) メッセージを直接送ることができます。

Editor\_SetOutlineArray( HWND hwnd, INT\_PTR nStartLine, INT\_PTR nCount, BYTE\* pLevelData );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nStartLine_

複数行の最初の行を指定します。

_nCount_

複数行の行数を指定します。

_pLevelData_

アウトライン レベルを指定する BYTE の配列を指定します。

## 戻り値

変更が無い場合には FALSE が返されます。それ以外では TRUE が返されます。

## バージョン

Version 13 以上で利用できます。
