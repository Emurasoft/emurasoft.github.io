# CONVERT\_CSV\_INFO

[EE\_CONVERT\_CSV](../message/ee_convert_csv) メッセージで使用します。

typedef struct \_CONVERT\_CSV\_INFO {

UINT cbSize;

int iDestMode;

UINT nFlags;

int nSepCount;

const int\* pcxSepWidths;

} CONVERT\_CSV\_INFO;

## フィールド

_cbSize_

sizeof( CONVERT\_CSV\_INFO ) を指定します。

_iDestMode_

Specifies the index of the CSV format you want to convert the current document to. 0 means fixed-width columns format (non-CSV). 1 means the first defined format in the CSV tab of the Customize dialog box (Comma separeted by default).

_nFlags_

次の値の組み合わせを指定することができます。

| 値 | 意味 |
| --- | --- |
| CSV\_HALF\_WIDTH | Assumes all half-width characters to improve the speed. |
| CSV\_DISCARD\_UNDO | Discards undo information to improve the speed. |

_nSepCount_

If the current document is a non-CSV document, and if you want to convert the current document of fixed-width columns to a CSV document, this parameter specifies the number of separators, and it must be equal to the size of the array specified in the _pcxSepWidths_ parameter. This parameter is ignored if the current document is a CSV document.

_pcxSepWidths_

Specifies the array of integers representing the widths between separators if the _nSepCount_ parameter is non-zero.

## バージョン

EmEditor Professional Version 19.8 以上で利用できます。
