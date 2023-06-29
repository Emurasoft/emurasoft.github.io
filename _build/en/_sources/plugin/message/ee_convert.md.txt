# EE\_CONVERT

Converts characters. You can send this message explicitly or use the
[Editor\_Convert](../macro/editor_convert) inline function.

EE\_CONVERT

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szChars;

## Parameters

_nFlags_

> You can specify a combination of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | FLAG\_MAKE\_LOWER | Converts to lowercase characters. |
> | FLAG\_MAKE\_UPPER | Converts to uppercase characters. |
> | FLAG\_HAN\_TO\_ZEN | Converts to full-size characters. |
> | FLAG\_ZEN\_TO\_HAN. | Converts to half-size characters |
> | FLAG\_CAPITALIZE | Capitalizes the first letter of each word. |
> | FLAG\_MAKE\_LOWER\_L | Converts to lowercase characters (locale-dependent). |
> | FLAG\_MAKE\_UPPER\_L | Converts to uppercase characters (locale-dependent). |
> | FLAG\_CAPITALIZE\_L | Capitalizes the first letter of each word (locale-dependent). |
> | FLAG\_CONVERT\_SELECT\_ALL | Converts the entire text. If this flag is not set, EE\_CONVERT converts <br> the characters only in the selection. |
> | FLAG\_CONVERT\_KATA | Converts Katakana. |
> | FLAG\_CONVERT\_ALPHANUMERIC | Converts Alphabets and numeric characters. |
> | FLAG\_CONVERT\_MARK | Converts marks. |
> | FLAG\_CONVERT\_SPACE | Converts spaces. |
> | FLAG\_CONVERT\_KANA\_MARK | Converts Kana marks. |
> | FLAG\_CONVERT\_CUSTOM | When FLAG\_HAN\_TO\_ZEN or FLAG\_ZEN\_TO\_HAN is specified, the szChars parameter specifies which individual characters should be converted. If this value is specified, you must also specify the szChars parameter, and FLAG\_CONVERT\_KATA, FLAG\_CONVERT\_ALPHANUMERIC, FLAG\_CONVERT\_MARK, FLAG\_CONVERT\_SPACE, FLAG\_CONVERT\_KANA\_MARK values are ignored. |
> | FLAG\_JAPANESE\_YEN | Converts U+005C (REVERSE SOLIDUS) to U+FFE5 (FULLWIDTH YEN SIGN), and vice versa. |
> | FLAG\_KOREAN\_WON | Converts U+005C (REVERSE SOLIDUS) to U+FFE6 (FULLWIDTH WON SIGN), and vice versa. |
> | FLAG\_RIGHT\_SINGLE\_QUOTATION | Converts U+0027 (APOSTROPHE) to U+2019 (RIGHT SINGLE QUOTATION MARK), and vice versa. |
> | FLAG\_RIGHT\_DOUBLE\_QUOTATION | Converts U+0022 (QUOTATION MARK) to U+201D (RIGHT DOUBLE QUOTATION MARK), and vice versa. |

_szChars_

> You can set a combination of individual full-width characters you want to convert if FLAG\_CONVERT\_CUSTOM is specified. Set this parameter NULL if not used.

## Return Values

> If the message succeeds, the return value is nonzero. If the message fails,
> the return value is zero.