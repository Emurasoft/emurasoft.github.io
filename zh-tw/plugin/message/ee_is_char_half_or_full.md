# EE\_IS\_CHAR\_HALF\_OR\_FULL

決定以（1）UTF-16字元值或（2）縮放器值表示的指定字元是半形還是全形字元。（3）它也可以計算指定字串的總寬度。你可以明確地發送該消息或使用 [Editor\_IsCharHalfOrFull](../macro/editor_ischarhalforfull) 內嵌函式。

(1) EE\_IS\_CHAR\_HALF\_OR\_FULL

(WCHAR)wParam = ch

(int)lParam = 0

(2) EE\_IS\_CHAR\_HALF\_OR\_FULL

(UINT)wParam = nScaler

(int)lParam = -1

(3) EE\_IS\_CHAR\_HALF\_OR\_FULL

(INT\_PTR)wParam = cchStr

(LPCWSTR)lParam = pStr

## 參數

_ch_

要查詢的 Unicode 字元。

_ch_

（1）表示為 UTF-16 字元值的要查詢的 Unicode 字元。

_nScaler_

(2) 表示為縮放器值的要查詢的 Unicode 字元。

_pStr_

(3) 要查詢的 UTF-16 字串。

_cchStr_

(3) 要查詢的字串的長度，以字元為單位。

## 返回值

(1) 返回 1 如果 _ch_ 是一個半形字元，或返回 2 如果 _ch_ 是一個全形字元或是一個或高或低的 Surrogate 字元。如果指定的字元不提前字元位置，它可能會返回 0。

(2) 返回 1 如果 _nScaler_ 是一個半形字元，或返回 2 如果 _nScaler_ 是一個全形字元。如果指定的字元不提前字元位置，它可能會返回 0。

(3) 返回指定字串和長度的總寬度數。
