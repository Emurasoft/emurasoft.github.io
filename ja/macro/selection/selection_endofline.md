# EndOfLine メソッド (Selection オブジェクト)

現在行の最後に移動します。

## 

### \[JavaScript\]

```
document.selection.EndOfLine( [ bExtend [, nFlags ] ] );
```

### \[VBScript\]

```
document.selection.EndOfLine [ bExtend [, nFlags ] ]
```

## 引数

_bExtend_

省略可能。選択範囲を解除するかどうかを指定します。省略すると、選択範囲を解除して移動します。

_nFlags_

省略可能。次のうちのいずれかを指定します。

|     |     |
| --- | --- |
| eeLineView | 表示行を指定します。 |
| eeLineLogical | 論理行を指定します。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
