# Editor\_IsCharHalfOrFull

决定以（1）UTF-16字符值或（2）缩放器值表示的指定字符是半角还是全角字符。（3）它也可以计算指定字符串的总宽度。你能直接用该内联函数或明确地发送
[EE\_IS\_CHAR\_HALF\_OR\_FULL](../message/ee_is_char_half_or_full) 消息。

(1) Editor\_IsCharHalfOrFull( HWND hwnd, WCHAR ch );

(2) Editor\_IsCharHalfOrFull( HWND hwnd, UINT nScaler );

(3) Editor\_IsCharHalfOrFull( HWND hwnd, LPCWSTR pStr, INT\_PTR cchStr )

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_ch_

> （1）表示为 UTF-16 字符值的要查询的 Unicode 字符。

_nScaler_

> (2) 表示为缩放器值的要查询的 Unicode 字符。

_pStr_

> (3) 要查询的 UTF-16 字符串。

_cchStr_

> (3) 要查询的字符串的长度，以 UTF-16 字符数为单位。

## 返回值

> (1) 返回 1 如果 _ch_ 是一个半角字符，或返回 2 如果 _ch_ 是一个全角字符或是一个或高或低的代理项字符。如果指定的字符不提前字符位置，它可能会返回 0。
>
> (2) 返回 1 如果 _nScaler_ 是一个半角字符，或返回 2 如果 _nScaler_ 是一个全角字符。如果指定的字符不提前字符位置，它可能会返回 0。
>
> (3) 返回指定字符串和长度的总宽度数。