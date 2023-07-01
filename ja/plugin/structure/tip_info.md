# TIP\_INFO

[EE\_SHOW\_TIP](../message/ee_show_tip) メッセージで使用します。

typedef struct \_TIP\_INFO {

UINT cbSize;

LPCWSTR pszTip;

POINT\_PTR ptCaret;

POINT ptDev;

UINT nFlags;

} TIP\_INFO;

## フィールド

_cbSize_

> このデータ構造体のサイズ、sizeof( TIP\_INFO )を指定します。

_pszTip_

> ツールチップに表示するテキストを指定します。テキストの長さは 3,999 文字を超えることができません。文字列には、次の形式を使用して、クリック可能なテキストを含めることができます: "<a href="url">clickable text</a>"

_ptCaret_

> 現在、使用されていません。

_ptDev_

> 現在、使用されていません。

_nFlags_

> 次の値の組み合わせを指定します。
>
> |     |     |
> | --- | --- |
> | SHOW\_TIP\_ACTIVE\_STRING | マウス ポインターがポイントされているアクティブな文字列にツールチップを表示します。 |
> | SHOW\_TIP\_CURRENT\_CARET | キャレット位置にツールチップを表示します。 |
> | SHOW\_TIP\_CURRENT\_MOUSE | マウス ポインター位置にツールチップを表示します。 |
> | SHOW\_TIP\_HIDE | 既にツールチップが表示されている場合、非表示にします。 |

## バージョン

> Version 16.9 以上で利用できます。
