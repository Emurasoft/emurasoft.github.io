# Delete メソッド ()

選択範囲を削除します。選択が空の場合は、右側の指定した文字数だけ削除します。

#### \[JavaScript\]

document.selection. **Delete**( \[\[ _nCount_ \], _bComplete_ \] );

#### \[VBScript\]

document.selection. **Delete** \[\[ _nCount_ \], _bComplete_ \]

## 引数

_nCount_

省略可能。右側に削除する文字数を指定します。省略すると、1 を指定することになります。0 より小さい数を指定すると、 [DeleteLeft \
メソッド](selection_deleteleft) のように動作します。0 を指定すると、1 を指定したように動作します。

_bComplete_

省略可能。CSV セルモードの場合、区切り文字も含めて完全に削除するかどうかを指定します。省略すると、False を指定することになります。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。