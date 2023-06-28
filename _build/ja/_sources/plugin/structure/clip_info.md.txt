# CLIP\_INFO

[EE\_CLIP\_HISTORY](../message/ee_clip_history) メッセージで使用します。

typedef struct \_CLIP\_INFO {

size\_t cbSize;

LPWSTR pszBuf;

UINT cchBuf;

UINT iPos;

UINT nAction;

UINT nFlags;

} CLIP\_INFO;

## フィールド

_cbSize_

> このデータ構造体のバイトのサイズ。 [EE\_CLIP\_HISTORY](../message/ee_clip_history) メッセージを送る前にこのメンバーを sizeof( CLIP\_INFO ) に設定します。

_pszBuf_

> テキストまたは入力されたテキストを受信するバッファを指定します。

_cchBuf_

> 終端 NULL 文字を含めた文字のバッファのサイズを指定します。

_iPos_

> クリップボード履歴にある位置を指定します。 _nAction_ が CI\_GET\_CLIP を指定してるときに (UINT)-1 を指定すると、クリップボード履歴ではなく実際のクリップボードの中身を取得します。

_nAction_

> 値を下記の中からひとつ指定します。しかし、 CI\_INSERT\_CLIP のみ CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP と組み合わせることができます。
>
> |     |     |
> | --- | --- |
> | CI\_GET\_CLIP | クリップボード履歴にある特定の位置でテキストを取り込みます。 |
> | CI\_INSERT\_CLIP | クリップボード履歴にある特定の位置でテキストを入力します。 |
> | CI\_REMOVE\_CLIP | クリップボード履歴にある特定の位置でテキストを消去します。 |
> | CI\_GET\_POS | クリップボード履歴にある現在の位置でテキストを取り込みます。 |
> | CI\_SET\_POS | クリップボード履歴にある現在の位置でテキストを設定します。 |
> | CI\_ROTATE\_CLIP | クリップボード履歴にある現在の位置でテキストを回転させます。 |
> | CI\_MOVE\_CLIP | クリップボード履歴にある指定の位置を別の位置に移動します。 |
> | CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP | 現在のクリップボードの内容からクリップボード履歴によって置換されることを防ぎます。この値は CI\_INSERT\_CLIP との組み合わせで使用されます。 |

_nFlags_

> When nAction が CI\_INSERT\_CLIP または CI\_REMOVE\_CLIP の場合、この値は入力または消去されたクリップボード フォーマットで指定します。 nAction が CI\_GET\_CLIP の場合、この値は実際のクリップボード フォーマットで満たされます。nAction が CI\_MOVE\_CLIP の場合、移動先の位置を指定します。そうでなければ、この値は無視され、０になります。この値が必要な場合は下記の中の一つになります。
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 文字単位で通常に選択されています |
> | SEL\_TYPE\_LINE | 行単位で選択されています |
> | SEL\_TYPE\_BOX | 箱型選択されています |

## バージョン

> Version 9.00 以上で利用できます。