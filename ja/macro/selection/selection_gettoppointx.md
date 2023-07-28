# GetTopPointX メソッド (Selection オブジェクト)

選択範囲の最初の現在桁を 1 で始まる整数で返します。

## 

### \[JavaScript\]

```
xPos = document.selection.GetTopPointX( nFlags [, iSel ] );
```

### \[VBScript\]

```
xPos = document.selection.GetTopPointX( nFlags [, iSel ] )
```

## 引数

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eePosView | 表示上の桁数を返します。 |
| eePosLogical | 実際の改行コード位置 (最初の行の場合、文書の先頭) からの文字数を返します。 |
| eePosLogicalA | eePosLogical と同じですが、全角文字を 2 と数えます。 |
| eePosCell | CSV セル単位 |

_iSel_

省略可能。複数選択の場合、1 から始まる選択のインデックスを指定します。0 を指定するか省略すると、通常の選択を指定します。1 以上を指定した場合、 _nFlags_ には eePosLogical を指定する必要があります。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
