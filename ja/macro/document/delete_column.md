# DeleteColumn メソッド ()

CSV モードで指定された列を削除します。

## 

### \[JavaScript\]

```
document.DeleteColumn( iColumn, [ iColumn2 ] );
```

### \[VBScript\]

```
document.DeleteColumn iColumn, [ iColumn2 ]
```

## パラメータ

_iColumn1_

削除する最初の列を指定します。

_iColumn2_

削除する最後の列を指定します。省略すると iColumn1 で指定された 1列のみが削除されます。

## 例

次の例は、3列目から5列目を削除します。

### \[JavaScript\]

```
document.DeleteColumn( 3, 5 );
```

### \[VBScript\]

```
document.DeleteColumn 3, 5
```

## バージョン

EmEditor Professional Version 21.0 以上で利用できます。
