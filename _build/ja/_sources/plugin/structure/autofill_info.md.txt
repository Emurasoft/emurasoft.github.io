# AUTOFILL\_INFO

[EE\_AUTOFILL](../message/ee_autofill) メッセージで使用します。

typedef struct \_AUTOFILL\_INFO {

UINT cbSize;

POINT\_PTR ptSrcCellStart;

POINT\_PTR ptSrcCellEnd;

POINT\_PTR ptDestCellStart;

POINT\_PTR ptDestCellEnd;

DWORD dwFlags;

INT64 nIncrement;

} AUTOFILL\_INFO;

## フィールド

_cbSize_

> このデータ構造体のバイトのサイズ。 [EE\_AUTOFILL](../message/ee_autofill) メッセージを送る前にこのメンバーを sizeof( AUTOFILL\_INFO ) に設定します。

_ptSrcCellStart_

> 元のセルの開始位置を指定します。

_ptSrcCellEnd_

> 元のセルの終了位置を指定します。

_ptDestCellStart_

> 目標のセルの開始位置を指定します。

_ptDestCellEnd_

> 目標のセルの終了位置を指定します。

_dwFlags_

> 次の値の組み合わせを指定します。
>
> |     |     |
> | --- | --- |
> | FLAG\_FILL\_DEFAULT | EmEditor が目標のセルに入力する値を決定します。 |
> | FLAG\_FILL\_COPY | ソース範囲からターゲット範囲に値をコピーし、必要に応じて繰り返します。 |
> | FLAG\_FILL\_SERIES | ソース範囲の値をターゲット範囲に連続する数値として適用します。 |
> | FLAG\_FILL\_FLASH | フラッシュ フィルの動作を実行します。つまり、検出されたパターンに基づいて、ソース範囲の値をターゲット範囲に適用します。このフラグは垂直方向にのみ適用されます。 |
> | FLAG\_FILL\_DONT\_OVERWRITE | オートフィルの動作はターゲット範囲にある既存のセルを上書きしないこととします。これは FLAG\_FILL\_FLASH と共に使用することはできません。 |
> | FLAG\_FILL\_REPEAT | オートフィルの動作は最終行まで空でないセルの値を使用して繰り返されます。これは FLAG\_FILL\_FLASH と共に使用することはできません。 |

_nIncrement_

> 単一のセルのみ選択されていて、 _dwFlags_ フィールドに FLAG\_FILL\_SERIES が指定されている場合、連番の増加数を指定します。

## バージョン

> Version 17.5 以上で利用できます。