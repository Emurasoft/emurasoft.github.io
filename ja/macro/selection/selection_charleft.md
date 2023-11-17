# CharLeft メソッド (Selection オブジェクト)

カーソル位置を左に指定した文字数だけ移動します。

## 

### \[JavaScript\]

```
document.selection.CharLeft( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.CharLeft [ bExtend [, nCount ] ]
```

## パラメータ

_bExtend_

省略可能。選択範囲を解除するかどうかを指定します。省略すると、選択範囲を解除して移動します。

_nCount_

省略可能。左に移動する文字数を指定します。省略すると、1 文字だけ左に移動します。0 より小さい数を指定すると、 [CharRight メソッド](selection_charright) のように動作します。0 を指定すると、1 を指定したように動作します。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
