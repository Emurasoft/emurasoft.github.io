# Filters コレクション

Filters コレクションは、 [Filter オブジェクト](../filter/index) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| [Count](count) | アイテムの数を取得します。 |
| [Item](item) | 指定したインデックスの [Filter オブジェクト](../filter/index) を取得します。 |
| [VisibleLinesAbove](visible_lines_above) | 一致した行の上に表示する行数を指定します。 |
| [VisibleLinesBelow](visible_lines_below) | 一致した行の下に表示する行数を指定します。 |

## メソッド

|     |     |
| --- | --- |
| [Add](add) | アイテムを追加します。 |
| [AddFind](add_find) | 検索するアイテムを追加します。 |
| [AddReplace](add_replace) | 置換するアイテムを追加します。 |
| [Clear](clear) | コレクションのすべてのアイテムを削除します。 |
| [Export](export) | コレクションを TSV ファイルにエクスポートします。 |
| [Import](import) | TSV ファイルをコレクションにインポートします。 |
| [Remove](remove) | アイテムを削除します。 |

## 例

#### \[JavaScript\]

list = new Enumerator( document.filters );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.Value );

}

#### \[VBScript\]

For Each item In document.filters

alert item.Value

Next

## バージョン

EmEditor Professional Version 16.0 以上で利用できます。


```{toctree}
:maxdepth: 1
add
add_find
add_replace
clear
count
export
import
item
remove
visible_lines_above
visible_lines_below
```
