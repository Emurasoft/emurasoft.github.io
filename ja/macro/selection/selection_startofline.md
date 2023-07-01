# StartOfLine メソッド ()

カーソル位置を行の最初に移動します。

#### \[JavaScript\]

document.selection. **StartOfLine**( \[ _bExtend_ \[, _nFlags_ \] \]
);

#### \[VBScript\]

document.selection. **StartOfLine** \[ _bExtend_ \[, _nFlags_ \] \]

## 引数

_bExtend_

省略可能。選択範囲を解除するかどうかを指定します。省略すると、選択範囲を解除して移動します。

_nFlags_

省略可能。次のうちのいずれかを指定します。

|     |     |
| --- | --- |
| eeLineView | 表示行を指定します。 |
| eeLineLogical | 論理行を指定します。 |
| eeLineHomeText | 行頭またはテキスト開始位置へ移動します。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
