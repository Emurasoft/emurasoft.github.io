# GetAnchorPointX メソッド ()

選択範囲の開始位置の現在桁を 1 で始まる整数で返します。

#### \[JavaScript\]

xPos = document.selection. **GetAnchorPointX**( _nFlags_ );

#### \[VBScript\]

xPos = document.selection. **GetAnchorPointX**( _nFlags_ )

## 引数

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eePosView | 表示上の桁数を返します。 |
| eePosLogical | 実際の改行コード位置 (最初の行の場合、文書の先頭) からの文字数を返します。 |
| eePosLogicalA | eePosLogical と同じですが、全角文字を 2 と数えます。 |
| eePosCell | CSV セル単位 |

## バージョン

EmEditor Professional Version 4.03 以上で利用できます。
