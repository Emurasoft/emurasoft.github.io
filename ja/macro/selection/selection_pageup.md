# PageUp メソッド (Selection オブジェクト)

1 ページ上へ移動します。

## 

### \[JavaScript\]

```
document.selection.PageUp( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.PageUp [ bExtend [, nCount ] ]
```

## 引数

_bExtend_

省略可能。選択範囲を解除するかどうかを指定します。省略すると、選択範囲を解除して移動します。

_nCount_

省略可能。上に移動するページ数を指定します。省略すると、1 ページだけ上に移動します。0 より小さい数を指定すると、 [PageDown \
メソッド](selection_pagedown) のように動作します。0 を指定すると、1 を指定したように動作します。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
