# EE\_ENUM\_HIGHLIGHT

強調文字列の一覧を取得します。このメッセージを直接送るか、または [Editor\_EnumHighlight インライン関数](../macro/editor_enumhighlight) を使うことができます。

EE\_ENUM\_HIGHLIGHT

wParam = (WPARAM) (size\_t) cchBuf;

lParam = (LPARAM) (LPWSTR) pBuf;

## パラメータ

_cchBuf_

バッファのサイズを文字単位で指定します。バッファの最後には、ヌル文字 2 個分を確保する必要があります。0
を指定すると、必要なバッファのサイズを取得します。

_pBuf_

強調文字列の一覧を取得するバッファを指定します。このバッファに利用可能な設定がヌル文字で区切られて格納されます。最後の設定の後には、ヌル文字が 2
個格納されます。cchBuf に 0 を指定した場合は、pBuf を NULL に指定することができます。

各文字列の最初の文字は、色と次の値の組み合わせになります。

|     |     |
| --- | --- |
| 0 から 9 まで | 色。この値をマスクするには HIGHLIGHT\_COLOR\_MASK を使用します。 |
| HIGHLIGHT\_WORD | 単語のみ。 |
| HIGHLIGHT\_RIGHT\_SIDE | 行の右を強調。 |
| HIGHLIGHT\_INSIDE\_TAG | タグの内側のみ。 |
| HIGHLIGHT\_REG\_EXP | 正規表現。 |
| HIGHLIGHT\_CASE | 大文字小文字を区別。 |
| HIGHLIGHT\_RIGHT\_ALL | 行の右全部を強調。 |

## 戻り値

必要なバッファのサイズが返されます。

## バージョン

Version 7.00 以上で利用できます。
