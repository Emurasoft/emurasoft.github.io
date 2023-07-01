# Editor\_IsCharHalfOrFull

Determines whether a specified character expressed as a (1) UTF-16 character value or (2) scaler value is a half-width or full-width
character. (3) It can also count the total widths of the specified string. You can use this inline function or explicitly send the
[EE\_IS\_CHAR\_HALF\_OR\_FULL](../message/ee_is_char_half_or_full) message.

(1) Editor\_IsCharHalfOrFull( HWND hwnd, WCHAR ch );

(2) Editor\_IsCharHalfOrFull( HWND hwnd, UINT nScaler );

(3) Editor\_IsCharHalfOrFull( HWND hwnd, LPCWSTR pStr, INT\_PTR cchStr )

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_ch_

> (1) The Unicode character to be queried expressed as a UTF-16 character value.

_nScaler_

> (2) The Unicode character to be queried expressed as a scaler value.

_pStr_

> (3) The UTF-16 string to be queried.

_cchStr_

> (3) The length of the string in UTF-16 characters to be queried.

## Return Values

> (1) Returns 1 if _ch_ is a halfwidth character, or returns 2 if _ch_ is a fullwidth or a high or low surrogate character. It may return 0 if the specified character does not advance the character position.
>
> (2) Returns 1 if _nScaler_ is a halfwidth character, or returns 2 if _nScaler_ is a fullwidth character. It may return 0 if the specified character does not advance the character position.
>
> (3) Returns the total number of widths of the specified string and length.
