# GetBottomPointY メソッド ()

選択範囲の最後の現在行を 1 で始まる整数で返します。

#### \[JavaScript\]

yPos = document.selection. **GetBottomPointY**( _nFlags_ \[, _iSel_ \] );

#### \[VBScript\]

yPos = document.selection. **GetBottomPointY**( _nFlags_ \[, _iSel_ \] )

## 引数

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eePosView | 表示上、何行目かを返します。 |
| eePosLogical | 実際の改行コード位置で区切って何行目かを返します。 |
| eePosCellLogical | CSV セル単位 (論理座標) |
| eePosCellView | CSV セル単位 (表示座標) |

_iSel_

省略可能。複数選択の場合、1 から始まる選択のインデックスを指定します。0 を指定するか省略すると、通常の選択を指定します。1 以上を指定した場合、 _nFlags_ には eePosLogical を指定する必要があります。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
