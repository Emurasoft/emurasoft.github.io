# SetActivePoint メソッド ()

カーソル位置を設定します。

#### \[JavaScript\]

document.selection. **SetActivePoint**( _nFlags_, _xPos_, _yPos_ \[ \[, _bExtend_ \] , iSel \] );

#### \[VBScript\]

document.selection. **SetActivePoint** _nFlags_, _xPos_, _yPos_ \[ \[, _bExtend_ \] , iSel \]

## 引数

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eePosView | 表示上の行、桁数で指定します。 |
| eePosLogical | 実際の改行コード位置 (最初の行の場合、文書の先頭) からの行、文字数で指定します。 |
| eePosLogicalA | eePosLogical と同じですが、全角文字を 2 と数えます。 |
| eePosCellLogical | CSV セル単位 (論理座標) |
| eePosCellView | CSV セル単位 (表示座標) |

_xPos_

カーソル位置の現在桁を 1 で始まる整数で指定します。

_yPos_

カーソル位置の現在行を 1 で始まる整数で指定します。

_bExtend_

省略可能。選択範囲を伸縮するかどうかを指定します。bExtend が true
の場合、カーソルが指定する位置に移動しますが、選択範囲の最初の位置は変わりません。false の場合、両方とも指定する位置に移動します。

_iSel_

省略可能。複数選択の場合、1 から始まる選択のインデックスを指定します。0 を指定するか省略すると、通常の選択を指定します。1 以上を指定した場合、 _nFlags_ には eePosLogical を指定する必要があります。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。ただし、 _bExtend_ パラメータは
Version 4.03 以上で追加されました。
