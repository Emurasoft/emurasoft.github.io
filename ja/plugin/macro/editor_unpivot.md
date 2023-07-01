# Editor\_Unpivot

CSV データを平らにして行に変換します。このインライン関数を使うか、または [EE\_UNPIVOT](../message/ee_unpivot) メッセージを直接送ることができます。

HRESULT Editor\_PivotTable( HWND hwnd, int iRow, int iColumn, int iValue, UINT nFlags, UINT nSortRow, UINT nSortColumn, LPCWSTR pszLocale, LPCWSTR pszTotalRowLabel, LPCWSTR pszTotalColLabel, int nDecimalPlaces );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

> 使用されません。0 である必要があります。

_pszSelect_

> ピボット解除する列を選択する文字列を指定します。例: "2-5"、"3-"、"1,3,5"。このフィールドは空にすることができません。

_pszAttrLabel_

> 属性として作成される列のヘディングのラベルを指定します。

_pszValueLabel_

> 値として作成される列のヘディングのラベルを指定します。

_nFooter_

> フッターの行数を指定します。フッターの領域は変換されません。

## 戻り値

> 失敗すると負の値を返します。

## バージョン

> Version 21.4 以上で利用できます。
