# MoveColumn メソッド (Document オブジェクト)

CSV モードで指定された列を移動またはコピーします。

## 

### \[JavaScript\]

```
document.MoveColumn( iColumn, iColumn2, iColumnTo [ , nFlags ] );
```

### \[VBScript\]

```
document.MoveColumn iColumn, iColumn2, iColumnTo [ , nFlags ]
```

## パラメータ

_iColumn1_

移動またはコピーする最初の列を指定します。

_iColumn2_

移動またはコピーする最後の列を指定します。

_iColumnTo_

どの列の前に移動またはコピーするかを指定します。

_nFlags_

次の値のいずれかを指定することができます。

| 値 | 意味 |
| --- | --- |
| eeColumnMove | _iColumn1_ から _iCollumn2_ までの列を _iColumnTo_ の前に移動します。 |
| eeColumnCopy | _iColumn1_ から _iCollumn2_ までの列を _iColumnTo_ の前にコピーします。 |

## 例

次の例は、3列目を左端に移動します。

### \[JavaScript\]

```
document.MoveColumn( 3, 3, 1 );
```

### \[VBScript\]

```
document.MoveColumn 3, 3, 1
```

## バージョン

EmEditor Professional Version 19.7 以上で利用できます。
