# Editor\_GetPageSize

1ページのサイズを取得します。このインライン関数を使うか、または [EE\_GET\_PAGE\_SIZE](../message/ee_get_page_size) メッセージを直接送ることができます。

Editor\_GetPageSize( HWND hwnd, SIZE\_PTR\* psizePage );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_psizePage_

1ページに表示できる行数と桁数を表す [SIZE\_PTR 構造体](../structure/size_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。
