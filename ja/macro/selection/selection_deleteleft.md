# DeleteLeft メソッド (Selection オブジェクト)

選択範囲を削除します。選択が空の場合は、左側の指定した文字数だけ削除します。

## 

### \[JavaScript\]

```
document.selection.DeleteLeft( [ nCount ] );
```

### \[VBScript\]

```
document.selection.DeleteLeft [ nCount ]
```

## 引数

_nCount_

省略可能。左側に削除する文字数を指定します。省略すると、1 を指定することになります。0 より小さい数を指定すると、 [Delete メソッド](selection_delete) のように動作します。0 を指定すると、1 を指定したように動作します。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
