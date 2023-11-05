# EE\_IS\_CHAR\_HALF\_OR\_FULL

Determines whether a specified character expressed as a (1) UTF-16 character value or (2) scaler value is a half-width or full-width
character. (3) It can also count the total widths of the specified string. You can send this message explicitly or use the [Editor\_IsCharHalfOrFull](../macro/editor_ischarhalforfull) inline function.

(1) ```
EE_IS_CHAR_HALF_OR_FULL
(WCHAR)wParam = ch
(int)lParam = 0
(2) EE_IS_CHAR_HALF_OR_FULL
(UINT)wParam = nScaler
(int)lParam = -1
(3) EE_IS_CHAR_HALF_OR_FULL
(INT_PTR)wParam = cchStr
(LPCWSTR)lParam = pStr
```

## Parameters

_ch_

The Unicode character to be queried.

_ch_

(1) The Unicode character to be queried expressed as a UTF-16 character value.

_nScaler_

(2) The Unicode character to be queried expressed as a scaler value.

_pStr_

(3) The UTF-16 string to be queried.

_cchStr_

(3) The length of the string in characters to be queried.

## Return Values

(1) Returns 1 if _ch_ is a halfwidth character, or returns 2 if _ch_ is a fullwidth or a high or low surrogate character. It may return 0 if the specified character does not advance the character position.

(2) Returns 1 if _nScaler_ is a halfwidth character, or returns 2 if _nScaler_ is a fullwidth character. It may return 0 if the specified character does not advance the character position.

(3) Returns the total number of widths of the specified string and length.
