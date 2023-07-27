# Editor\_SetSelLength

選択テキストの長さを設定します。このインライン関数を使うか、または [EE\_SET\_SEL\_LENGTH メッセージ](../message/ee_set_sel_length) を直接送ることができます。

Editor\_SetSelLength( HWND hwnd, UINT nLen );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nLen_

選択テキストの長さを指定します。改行コードは、常に 2文字分 (CR+LF) となります。

## 戻り値

戻り値は利用されません。
