# Editor\_RotateClip

クリップボード履歴にある現在の位置を回転します。このインライン関数を使うか、または [EE\_CLIP\_HISTORY](../message/ee_clip_history) メッセージを直接送ることができます。

Editor\_RotateClip( HWND hwnd, int iDirection );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iDirection_

クリップボード履歴にある現在の位置を、どの方向に回転したいかを指定します。

## 戻り値

成功すると 1 で、失敗すると -1 です。

## バージョン

Version 9.00 以上で利用できます。
