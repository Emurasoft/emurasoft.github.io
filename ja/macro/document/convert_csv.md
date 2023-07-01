# ConvertCsv メソッド ()

CSV形式を変換します。

#### \[JavaScript\]

document. **ConvertCsv**( _iDestMode_, _nFlags_, _strSepPos_ );

#### \[VBScript\]

document. **ConvertCsv**( _iDestMode_, _nFlags_, _strSepPos_ );

## パラメータ

_iDestMode_

Specifies the index of the CSV format you want to convert the current document to. 0 means fixed-width columns format (non-CSV). 1 means the first defined format in the CSV tab of the Customize dialog box (Comma separeted by default).

_nFlags_

> 次の値の組み合わせを指定することができます。
>
> | 値 | 意味 |
> | --- | --- |
> | eeCsvHalfWidth | Assumes all half-width characters to improve the speed. |
> | eeCsvDiscardUndo | Discards undo information to improve the speed. |

_strSepCount_

> If the current document is a non-CSV document, and if you want to convert the current document of fixed-width columns to a CSV document, this string specifies the widths between separators, separated by commas. For instance, "10, 8" means 2 separators separated by 10 and 8 half-width characters. This parameter is ignored if the current document is a CSV document.

## 例

The following example converts a fixed-width columns to a comma-separated CSV format. The original fixed-width format is:

Madrid Spain   100

Paris  France  101

The destination CSV document will be:

Madrid,Spain,100

Paris,France,101

#### \[JavaScript\]

document.ConvertCsv( 1, 0, "7,8" );

#### \[VBScript\]

document.ConvertCsv 1, 0, "7,8"

## バージョン

EmEditor Professional Version 19.8 以上で利用できます。
