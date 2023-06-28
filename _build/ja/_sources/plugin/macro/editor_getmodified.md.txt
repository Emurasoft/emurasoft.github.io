# Editor\_GetModified

現在アクティブな文書が更新されているかどうかのフラグを取得します。このインライン関数を使うか、または
[EE\_GET\_MODIFIED](../message/ee_get_modified) メッセージを直接送ることができます。

Editor\_GetModified( HWND hwnd );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

## 戻り値

> 更新されている場合は TRUE を、更新されていない場合は FALSE を返します。