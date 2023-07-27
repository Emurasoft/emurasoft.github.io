# GetLine メソッド ()

指定する行のテキストを取得します。

## 

### \[JavaScript\]

```
str = document.GetLine( yLine [, nFlags ] );
```

### \[VBScript\]

```
str = document.GetLine( yLine [, nFlags ] )
```

## パラメータ

_yLine_

取得するテキストの行番号を指定します。

_nFlags_

省略可能。次の値の組み合わせを指定します。何も値が指定されていない場合は、改行コードなしで論理座標が指定されることになります。

|     |     |
| --- | --- |
| eeGetLineView | 表示座標を指定します。 |
| eeGetLineWithNewLines | テキストに改行コードを追加します。 |

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
