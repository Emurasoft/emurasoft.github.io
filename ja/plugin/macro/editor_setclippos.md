# Editor\_SetClipPos

クリップボード履歴にある現在の位置を設定します。このインライン関数を使うか、または [EE\_CLIP\_HISTORY](../message/ee_clip_history) メッセージを直接送ることができます。

Editor\_SetClipPos( HWND hwnd, int iPos );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iPos_

> クリップボード履歴にある新しい位置を指定します。

## 戻り値

> クリップボード履歴にある現在の位置を取得します。失敗すると、戻り値は -1 です。

## バージョン

> EmEditor Version 9.00 以上で利用できます。
