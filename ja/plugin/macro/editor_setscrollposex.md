# Editor\_SetScrollPosEx

スクロールバーの位置を設定します。このインライン関数を使うか、または [EE\_SET\_SCROLL\_POS メッセージ](../message/ee_set_scroll_pos) を直接送ることができます。

Editor\_SetScrollPosEx( HWND hwnd, POINT\_PTR\* pptPos, BOOL bCanMoveCursor );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pptPos_

スクロールバーの位置を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_bCanMoveCursor_

TRUE の場合、プロパティで [**\[スクロールでカーソルも移動\]** チェック ボックス](../../dlg/properties/scroll/index) がチェックされている場合 、カーソル位置も移動します。FALSE の場合、カーソル位置は移動しません。

## 戻り値

戻り値は利用されません。

## バージョン

Version 5.00 以上で利用できます。
