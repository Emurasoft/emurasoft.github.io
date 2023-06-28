# Editor\_SetModified

文書が更新されているかどうかのフラグを設定します。このインライン関数を使うか、または
[EE\_SET\_MODIFIED メッセージ](../message/ee_set_modified) を直接送ることができます。

Editor\_SetModified( HWND hwnd, BOOL bModified );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_bModified_

> 更新されている状態にするには TRUE を、更新されていない状態にするには FALSE を指定します。

## 戻り値

> 戻り値は利用されません。