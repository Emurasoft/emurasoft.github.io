# Editor\_DocGetModified

指定する文書が更新されているかどうかのフラグを取得します。このインライン関数を使うか、または
[EE\_GET\_MODIFIED](../message/ee_get_modified) メッセージを直接送ることができます。

Editor\_DocGetModified( HWND hwnd, int iDoc );

Editor\_DocGetModified( HWND hwnd, HEEDOC hDoc );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iDoc_

> 対象となる文書の 0 を基底とするインデックスを指定します。-1 を指定すると、現在アクティブな文書を対象とします。

_hDoc_

> 対象となる文書へのハンドルを指定します。NULL を指定すると、現在アクティブな文書を対象とします。

## 戻り値

> 更新されている場合は TRUE を、更新されていない場合は FALSE を返します。
