# GetAnchorPointY メソッド ()

選択範囲の開始位置の現在行を 1 で始まる整数で返します。

#### \[JavaScript\]

yPos = document.selection. **GetAnchorPointY**( _nFlags_ );

#### \[VBScript\]

yPos = document.selection. **GetAnchorPointY**( _nFlags_ )

## 引数

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eePosView | 表示上、何行目かを返します。 |
| eePosLogical | 実際の改行コード位置で区切って何行目かを返します。 |
| eePosCellLogical | CSV セル単位 (論理座標) |
| eePosCellView | CSV セル単位 (表示座標) |

## バージョン

EmEditor Professional Version 4.03 以上で利用できます。
