# NUMBERING\_INFO

Used by
[EE\_NUMBERING message](../message/ee_numbering).

typedef struct \_NUMBERING\_INFO {

UINT cbSize;

UINT nFlags;

LPCWSTR pszFirst;

LPCWSTR pszInc;

INT64 nMaxLines;

} NUMBERING\_INFO;

## Fields

_cbSize_

> Specifies sizeof( NUMBERING\_INFO ).

_nFlags_

> You can specify a combination of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | NUM\_FLAG\_CAPITAL\_LETTERS | Inserts hexadecimal values in capital letters. |
> | NUM\_FLAG\_SKIP\_EMPTY\_LINES | Numbering will continue after empty lines, without numbering the empty lines during vertical selection mode or multiple selection mode. |
> | NUM\_FLAG\_RESTART\_NUM\_EMPTY | Numbering will restart from the first value after empty lines during vertical selection mode or multiple selection mode. |
> | NUM\_FLAG\_RESTART\_NUM\_DISCONTINUOUS | Numbering will restart from the first value at discontinuous lines during multiple selection mode. |
> | NUM\_FLAG\_DECIMAL | Inserts numbers in decimal notation. |
> | NUM\_FLAG\_HEXADECIMAL | Inserts numbers in hexadecimal notation. |
> | NUM\_FLAG\_OCTAL | Inserts numbers in octal notation. |
> | NUM\_FLAG\_BINARY | Inserts numbers in binary notation. |
> | NUM\_FLAG\_OTHER | Inserts characters instead of numbers. Starting with the number specified in <br>the _pszFirst_ parameter, this option inserts sequential characters using the <br>increment of the Unicode value specified in the _pszInc_ parameter. Only one <br>character can be inserted at each line. |

_pszFirst_

> Specifies an initial value or character to insert at the first line.

_pszInc_

> Specifies an increment in the decimal notation. This is the change in value between the first line and the second line.

_nMaxLines_

> Specifies the number of lines in the decimal notation.

## Version

> Supported on Version 19.1 or later.
