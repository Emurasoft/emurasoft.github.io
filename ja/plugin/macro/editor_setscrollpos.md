# Editor\_SetScrollPos

スクロールバーの位置を設定します。このインライン関数を使うか、または [EE\_SET\_SCROLL\_POS メッセージ](../message/ee_set_scroll_pos) を直接送ることができます。

Editor\_SetScrollPos( HWND hwnd, POINT\_PTR\* pptPos );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pptPos_

> スクロールバーの位置を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。カーソル位置は変更しません。

## 戻り値

> 戻り値は利用されません。
