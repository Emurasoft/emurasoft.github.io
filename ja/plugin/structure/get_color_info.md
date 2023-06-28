# GET\_COLOR\_INFO

[EE\_GET\_COLOR \
メッセージ](../message/ee_get_color) で使用します。

typedef struct \_GET\_COLOR\_INFO {

UINT cbSize;

BOOL bFind;

UINT nIndex;

COLORREF clrText;

COLORREF clrBack;

int nAttr;

} GET\_COLOR\_INFO;

## フィールド

_cbSize_

> \[In\] データ構造体をバイト単位で指定します。 [EE\_GET\_COLOR](../message/ee_get_color) メッセージを送信する前に、sizeof( GET\_COLOR\_INFO ) を指定します。

_bFind_

> \[in\] 検索の色を取得する場合には TRUE を、それ以外の部分の色を取得する場合には FALSE を指定します。

_nIndex_

> \[in\] 色を取得するインデックスを指定します。bFind が FALSE の場合、インデックスは MAX\_SMART\_COLOR より小さい値である必要があります。

_clrText_

> \[out\] [EE\_GET\_COLOR](../message/ee_get_color) メッセージから戻ると、このフィールドには文字色が格納されます。この値は、RGB値、または次のいずれかの値になります。
>
> |     |     |
> | --- | --- |
> | DEFAULT\_COLOR | Windows システム色が使用されます。 |
> | TRANSPARENT\_COLOR | 透明色です。 |

_clrBack_

> \[out\] [EE\_GET\_COLOR](../message/ee_get_color) メッセージから戻ると、このフィールドには背景色が格納されます。この値は、RGB値、または次のいずれかの値になります。
>
> |     |     |
> | --- | --- |
> | DEFAULT\_COLOR | Windows システム色が使用されます。 |
> | TRANSPARENT\_COLOR | 透明色です。 |

_nAttr_

> \[out\] [EE\_GET\_COLOR](../message/ee_get_color) メッセージから戻ると、このフィールドにはスタイルが格納されます。この値は、次のいずれかの値になります。
>
> |     |     |
> | --- | --- |
> | SMART\_COLOR\_FONT\_NORMAL | 通常のフォントです。 |
> | SMART\_COLOR\_FONT\_UNDERLINE | 下線付きフォントです。 |
> | SMART\_COLOR\_FONT\_BOLD | 太字フォントです。 |
> | SMART\_COLOR\_FONT\_ITALIC | 斜体フォントです。 |
> | SMART\_COLOR\_FONT\_WIGGLY | 波線が付いたフォントです。 |
> | SMART\_COLOR\_FONT\_DOTTED | 線の場合、点線です。 |

## バージョン

> Version 14.4 以上で利用できます。