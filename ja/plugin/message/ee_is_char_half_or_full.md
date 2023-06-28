# EE\_IS\_CHAR\_HALF\_OR\_FULL

指定する (1) UTF-16 で表現された、または (2) スカラ値で表現された文字が半角か全角かを調べます。(3) また、指定した文字列の幅の合計を数えることもできます。このメッセージを直接送るか、または
[Editor\_IsCharHalfOrFull インライン関数](../macro/editor_ischarhalforfull) を使うことができます。

(1) EE\_IS\_CHAR\_HALF\_OR\_FULL

(WCHAR)wParam = ch

(int)lParam = 0

(2) EE\_IS\_CHAR\_HALF\_OR\_FULL

(UINT)wParam = nScaler

(int)lParam = -1

(3) EE\_IS\_CHAR\_HALF\_OR\_FULL

(INT\_PTR)wParam = cchStr

(LPCWSTR)lParam = pStr

## パラメータ

_ch_

> 調べたい文字のコードを Unicode で指定します。

_ch_

> (1) 調べたい文字を UTF-16 の値で指定します。

_nScaler_

> (2) 調べたい文字をスカラ値で指定します。

_pStr_

> (3) 調べたい文字列を UTF-16 で指定します。

_cchStr_

> (3) 調べたい文字列の長さを UTF-16 の文字単位で指定します。

## 戻り値

> (1) 全角の場合、または上位または下位サロゲート文字の場合は 2、半角の場合は 1、位置を移動しない文字の場合は 0 を返します。
>
> (2) 全角の場合は 2、半角の場合は 1、位置を移動しない文字の場合は 0 を返します。
>
> (3) 指定した文字列の幅の合計を返します。