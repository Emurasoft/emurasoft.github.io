# Editor\_GetScrollPos

スクロールバーの位置を取得します。このインライン関数を使うか、または [EE\_GET\_SCROLL\_POS](../message/ee_get_scroll_pos) メッセージを直接送ることができます。

Editor\_GetScrollPos( HWND hwnd, POINT\_PTR\* pptPos );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pptPos_

> スクロールバー位置を格納するための [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。