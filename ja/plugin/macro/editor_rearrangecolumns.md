# Editor\_RearrangeColumns

CSV 列を再配置します。このインライン関数を使うか、または [EE\_REARRANGE\_COLUMNS](../message/ee_rearrange_columns)
メッセージを直接送ることができます。

Editor\_RearrangeColumns( HWND hwnd, UINT nColumnArraySize, const INT\* piColumn );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nSize_

_piColumn_ パラメータに指定する列の数を指定します。

_piColumn_

再配置する列の順番を示す整数の配列を指定します。例えば、「0, 2, 4」は、元の CSV 文書の 1番目、3番目、5番目の列を結果に含めることを示します。

## 戻り値

成功すると 0 を返します。失敗すると 0 以外を返します。
