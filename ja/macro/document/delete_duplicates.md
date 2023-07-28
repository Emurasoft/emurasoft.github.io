# DeleteDuplicates メソッド (Document オブジェクト)

重複行を削除またはブックマークします。

## 

### \[JavaScript\]

```
nCount = document.DeleteDuplicates( [ strColumns, [ flags ] ] );
```

### \[VBScript\]

```
nCount = document.DeleteDuplicates( [ strColumns, [ flags ] ] )
```

## パラメータ

_strFilter_

検索する文字列を指定します。

_strColumns_

CSV 文書がアクティブな場合、重複行を調べる列の 1 を基底とするインデックスの配列を文字列で指定します。 例えば、"1,3,5" は、1列目、3列目、および 5列目を意味します。重複行の削除またはブックマークの設定中、指定された列が調べられます。この文字列が空の場合、行全体が調べられます。CSV でない文書がアクティブな場合、空の文字列を指定する必要があります。省略すると、行全体が調べられます。

_flags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| eeAdjacentOnly | 隣接する行のみを調べます。このフラグは文書が既に並べ替えられている場合に使用すると便利です。 |
| eeBookmark | 重複行にブックマークを設定します。このフラグが指定されていない場合は、重複行を削除します。 |
| eeIgnoreEmptyCells | Ignores all empty cells when searching for duplicate lines in CSV documents. |
| eeIgnoreEmptyLines | 空行を無視します。 |
| eeIncludeAll | 各重複のすべての行を削除、または各重複のすべての行にブックマークを設定します。 |
| eeSortIgnoreCase | 大文字と小文字を区別しません。 |
| eeSortInspectSelOnly | 箱型選択または複数選択が存在する時、選択範囲の文字列のみを調べます。strColumns パラメータが指定されている場合、このフラグは無視されます。 |
| eeSortSelectionOnly | 選択範囲のみ調べます。 |

## 戻り値

戻り値は、見つかった重複行の数になります。

## バージョン

EmEditor Professional Version 16.4 以上で利用できます。
