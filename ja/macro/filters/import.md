# Import メソッド (Filters コレクション)

TSV ファイルをコレクションにインポートします。

## 

### \[JavaScript\]

```
list.Import( strFileName[, bAppend ] );
```

### \[VBScript\]

```
list.Import strFileName[, bAppend ]
```

## パラメータ

_strFileName_

TSV ファイルの完全パスを含むファイル名を指定します。

_bAppend_

メソッドがファイルをインポートして既存のフィルターにフィルターを追加するかどうかを指定します。省略すると False が指定されます。

## 例

### \[JavaScript\]

```
var filters = document.filters;
filters.Import( "E:\\Test\\filter.tsv" );
document.filters = filters;
```

### \[VBScript\]

```
Set filters = document.filters
filters.Import "E:\\Test\\filter.tsv"
document.filters = filters
```

## バージョン

EmEditor Professional Version 16.0 以上で利用できます。
