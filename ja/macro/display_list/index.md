# DisplayList コレクション

DisplayList コレクションは [DisplayItem オブジェクト](../display_item/index) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| **[Count](count)** | アイテムの数を取得します。 |
| **[Item](item)** | 指定のインデックスの [DisplayItem オブジェクト](../display_item/index) を取得します。 |

## 例

#### \[JavaScript\]

list = new Enumerator( document.Config.Display.ColorList );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.TextColor );

}

#### \[VBScript\]

For Each item In document.Config.Display.ColorList

alert item.TextColor

Next

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。


```{toctree}
:maxdepth: 1
count
item
```
