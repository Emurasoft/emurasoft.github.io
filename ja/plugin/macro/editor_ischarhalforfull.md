# Editor\_IsCharHalfOrFull

指定する (1) UTF-16 で表現された、または (2) スカラ値で表現された文字が半角か全角かを調べます。(3) また、指定した文字列の幅の合計を数えることもできます。このインライン関数を使うか、または
[EE\_IS\_CHAR\_HALF\_OR\_FULL メッセージ](../message/ee_is_char_half_or_full) を直接送ることができます。

(1) Editor\_IsCharHalfOrFull( HWND hwnd, WCHAR ch );

(2) Editor\_IsCharHalfOrFull( HWND hwnd, UINT nScaler );

(3) Editor\_IsCharHalfOrFull( HWND hwnd, LPCWSTR pStr, INT\_PTR cchStr )

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_ch_

> (1) The Unicode character to be queried expressed as a UTF-16 character value.

_nScaler_

> (2) The Unicode character to be queried expressed as a scaler value.

_pStr_

> (3) The UTF-16 string to be queried.

_cchStr_

> (3) The length of the string in UTF-16 characters to be queried.

## 戻り値

> (1) 全角の場合、または上位または下位サロゲート文字の場合は 2、半角の場合は 1、位置を移動しない文字の場合は 0 を返します。
>
> (2) 全角の場合は 2、半角の場合は 1、位置を移動しない文字の場合は 0 を返します。
>
> (3) 指定した文字列の幅の合計を返します。
