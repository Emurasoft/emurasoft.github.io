# SetAnchorPoint メソッド

選択範囲の開始位置を設定します。

#### \[JavaScript\]

document.selection. **SetAnchorPoint**( _nFlags_, _xPos_, _yPos_
);

#### \[VBScript\]

document.selection. **SetAnchorPoint** _nFlags_, _xPos_, _yPos_

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

## バージョン

EmEditor Professional Version 4.03 以上で利用できます。