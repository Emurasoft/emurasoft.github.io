# LineDown メソッド (Selection オブジェクト)

カーソル位置を下に指定した行数だけ移動します。

## 

### \[JavaScript\]

```
document.selection.LineDown( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.LineDown [ bExtend [, nCount ] ]
```

## 引数

_bExtend_

省略可能。選択範囲を解除するかどうかを指定します。省略すると、選択範囲を解除して移動します。

_nCount_

省略可能。下に移動する行数を指定します。省略すると、1 行だけ下に移動します。0 より小さい数を指定すると、 [LineUp \
メソッド](selection_lineup) のように動作します。0 を指定すると、1 を指定したように動作します。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
