# CsvList コレクション

CsvList コレクションは [Csv オブジェクト](../csv/index) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| **[Count](count)** | Csv オブジェクトの数を取得します。 |
| **[Item](item)** | 指定したインデックスの [Csv オブジェクト](../csv/index) を取得します。 |

## メソッド

|     |     |
| --- | --- |
| **[Add](add)** | アイテムを追加します。 |
| **[Insert](insert)** | アイテムを追加します。 |
| **[Remove](remove)** | アイテムを削除します。 |
| [**Reset**](reset) | コレクションをリセットします。 |

## 例

### \[JavaScript\]

```
csvs = new Enumerator( editor.CsvList );
for( ; !csvs.atEnd(); csvs.moveNext() ){
item = csvs.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In editor.CsvList
alert item.Name
Next
```

## バージョン

EmEditor Professional Version 19.4 以上で利用できます。


```{toctree}
:hidden:
:maxdepth: 1
add
count
insert
item
remove
reset
```
