# Indent メソッド (Selection オブジェクト)

選択範囲をインデントします。

## 

### \[JavaScript\]

```
document.selection.Indent( [ nCount ] );
```

### \[VBScript\]

```
document.selection.Indent [ nCount ]
```

## 引数

_nCount_

省略可能。インデントする回数を指定します。省略すると、1 個の Tab 分だけインデントします。0 より小さい数を指定すると、 [UnIndent メソッド](selection_unindent) のように動作します。0 を指定すると、1 を指定したように動作します。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
