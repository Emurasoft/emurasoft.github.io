# COLUMN\_INFO

[SORT\_INFO 構造体](sort_info) で使用します。

typedef struct \_COLUMN\_INFO {

int iCol;

UINT nFlags;

} COLUMN\_INFO;

## フィールド

_iCol_

> 並べ替える列を指定します。

_nFlags_

> 次の値の組み合わせを指定します。
>
> |     |     |
> | --- | --- |
> | SORT\_ASCEND | 昇順に並べ替えます。 |
> | SORT\_DESCEND | 降順に並べ替えます。 |
> | SORT\_DATE | 日付と時刻を並べ替えます。 |
> | SORT\_LENGTH | テキストの長さで並べ替えます。 |
> | SORT\_NUM | 数字を並べ替えます。 |
> | SORT\_TEXT | テキストを ABC 順で並べ替えます。 |
> | SORT\_WORDS | テキストを単語数で並べ替えます。 |

## バージョン

> Version 16.4 以上で利用できます。
