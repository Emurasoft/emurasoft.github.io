# WordLeft メソッド ()

カーソル位置を単語の左に移動します。

#### \[JavaScript\]

document.selection. **WordLeft**( \[ _bExtend_ \[, _nCount_ \] \] );

#### \[VBScript\]

document.selection. **WordLeft** \[ _bExtend_ \[, _nCount_ \] \]

## 引数

_bExtend_

省略可能。選択範囲を解除するかどうかを指定します。省略すると、選択範囲を解除して移動します。

_nCount_

省略可能。左に移動する単語数を指定します。省略すると、1 単語だけ左に移動します。0 より小さい数を指定すると、 [WordRight \
メソッド](selection_wordright) のように動作します。0 を指定すると、1 を指定したように動作します。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。