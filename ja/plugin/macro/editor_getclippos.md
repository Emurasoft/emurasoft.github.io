# Editor\_GetClipPos

クリップボード履歴にある現在の位置を取得します。このインライン関数を使うか、または [EE\_CLIP\_HISTORY](../message/ee_clip_history) メッセージを直接送ることができます。

Editor\_GetClipPos( HWND hwnd );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

## 戻り値

クリップボード履歴にある現在の位置を取得します。メッセージが失敗すると、戻り値は -1 です。

## バージョン

Version 9.00 以上で利用できます。
