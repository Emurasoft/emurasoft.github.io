# Editor\_SetSelView

選択テキストの開始位置と終了位置を設定します。このインライン関数を使うか、または [EE\_SET\_SEL\_VIEW メッセージ](../message/ee_set_sel_view) を直接送ることができます。

Editor\_SetSelView( HWND hwnd, POINT\_PTR\* pptSelStart, POINT\_PTR\* pptSelEnd );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pptSelStart_

選択テキストの開始位置を表す [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。位置は表示座標になります。

_pptSelEnd_

選択テキストの終了位置を表す [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。位置は表示座標になります。

## 戻り値

戻り値は利用されません。
